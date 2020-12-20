var fs     = require("fs");
var path   = require("path");
var parser = require("./log_parser.js");


// matches the value to the type of data
var matchType = function(value){ //String Integer Double
	if(/^\-?\d+\s*$/.test(value) || /^\-?\d+[ ]+[a-zA-Z%]+\s*$/.test(value)){
		return " [Integer] ";
	}
	else if(/^\-?\d+\.\d+e?[\+\-]?\d*\s*$/.test(value) || /^\-?\d+\.\d+e?[\+\-]?\d*[ ]+[a-zA-Z%]+\s*$/.test(value)){
		return " [Double] ";
	}
	else{
		return " [String] ";
	}
}

var numberOfProperties = function(obj){
	var count = 0;
    for(var prop in obj) {
        if(obj.hasOwnProperty(prop))
            ++count;
    }
    return count;
}

// adds the relevant data from the "STATUS" field
var interpretStatus = function(usedJson, testId, fileName){
	if(usedJson && usedJson[testId] && typeof usedJson[testId]["STATUS"] !== 'undefined'){
		var status = usedJson[testId]["output1"]["STATUS"];
		if(status.indexOf("Skipped") != -1){
			var skipMessage = status.match(/Skipped by (.*)/)
			if(skipMessage != null){
				skipMessage = skipMessage[1].trim();
			}
			else{	
				skipMessage = "ALWAYS_SKIP"
			}
			fs.appendFileSync(fileName,"\t\t#:run_mode = " + skipMessage + '\n');
		}
	}
}

exports.createTestFlow = function(parsedLog_detail, parsedLog_matched, fileName, callback){
	console.log("Creating Test Flow.")
	//hard coded starting info -- figure out how this changes later
	var startingInfo = "#LitePoint Test Flow Version 1.5.1 (2011-01-12)\n\nRunMode = 0\nRepeatTimes = 1\nExitWhenDone = 0\nShowFailInfo = 0\nPrecisionDigitMode = 0\nRetryMode = 0\nEnableFlowCheckWarning = 0\n";
	fs.writeFileSync(fileName, startingInfo);
	var string = "WIFI_11AC_MIMO_MPS:\n";
	fs.appendFileSync(fileName,string);

	// 
	for( testId in parsedLog_detail){
		var testIdWrite = testId.replace(/^\d+\.\s*/, '');
		fs.appendFileSync(fileName,'\t' + testIdWrite + '\n');

		// Write the input values
		fs.appendFileSync(fileName, '\t\t#Input Parameters:\n')
		if(parsedLog_detail[testId]["input"] != null){
			for(input in parsedLog_detail[testId]["input"]){
				var key = input;
				var value = parsedLog_detail[testId]["input"][input];
				var type = matchType(value);
				if( (type == " [Integer] ") || (type == " [Double] ") ){
					value = value.split(/[ ]{1,}/)[0];	//grab just the value, ignore the units
				}
				var formatted = "\t\t>" + key + type + ' = ' + value + ' \n';
				fs.appendFileSync(fileName,formatted);
			}
		}

		// Write the output values
		var usedJson = parsedLog_detail;
		fs.appendFileSync(fileName, '\t\t#Return Values:\n');
		if(testId.indexOf("TEST_RUN") != -1){
			interpretStatus(usedJson, testId, fileName);
			var errorMessage = usedJson[testId]["output1"]["ERROR_MESSAGE"];
			var formatted = "\t\t>ERROR_MESSAGE [String]  = <,> \n";
			fs.appendFileSync(fileName,formatted);
			continue;
		}

		else if(testId.indexOf("TEST_ADD") != -1 && parsedLog_matched[testId] != null){
			usedJson = parsedLog_matched;
		}
		
		if(usedJson[testId]["output1"] != null){
			for(output in usedJson[testId]["output1"]){
				if(output == "STATUS"){
					interpretStatus(usedJson, testId, fileName);
					continue;
				} 

				else if(output == "index"){ // ignore the index field
					continue;
				}

				var key = output.trim();
				if(key.indexOf(' ') != -1){	// some of the outputs have spaces in them for some return values that take up multiple lines.
					continue;				// Ignore them
				}

				var value = usedJson[testId]["output1"][output];
				var lowerLimit;
				var upperLimit;

				// Sometimes, the test item never ran, but in different runs it did. We just search through the outputs to find the first one that has a valid answer
				for(outputNum in usedJson[testId]){
					if(outputNum == "input"){
						continue;
					}
					if(usedJson[testId][outputNum][output] == null){
						continue;
					}
					value = usedJson[testId][outputNum][output];
					lowerLimit = "";
					upperLimit = "";
					if(value.constructor === Array){
						lowerLimit = value[1];
						upperLimit = value[2];
						value = value[0];
					}
					if(value != "" && value != "NO_VALUE"){
						break;
					}
				}

				value = value.replace(/\s*---\s*\[Failed\]\s*/, "");
				key = key.replace(/\.\d\d\d\./, '.');
				var type = matchType(value);
				var formatted = "\t\t<" + key + type + ' = ' + '<' + lowerLimit + ',' + upperLimit + '>\n';
				fs.appendFileSync(fileName,formatted);
			}
		}
	}
	if(callback && typeof callback == "function"){
		callback();
	}
}



if (typeof require != 'undefined' && require.main == module) {
	var args = process.argv.slice(2);
	if(args.length != 2 && args.length != 3){
		console.log("ERROR: Command line arguments invalid");
	}
	// with log file input
	else if(path.extname(args[0]) == '.txt' && args.length == 2){
		logFile = args[0];
		fileName = args[1];

		parser.fileparser(logFile, "", false, function(errStatus, parsedLog_detail, parsedLog_matched, returnErrorDetails){
			if(errStatus["error_code"] < 0){
				console.log("ERROR: Parsing Failed!");
			}
			else if(errStatus["error_code"] == 1){
				console.log("UNMATCHED OUTPUTS, Proceeding anyways");
			}
			else{
				exports.createTestFlow(parsedLog_detail, parsedLog_matched, fileName);
			}
		});
	}

	// with json file input
	else if(path.extname(args[0]) == '.json' && path.extname(args[1]) == '.json' && args.length == 3){
		var fileName = args[2];
		var jsonFile = fs.readFileSync(args[0]).toString();
		var parsedLog_detail = JSON.parse(jsonFile);
		jsonFile = fs.readFileSync(args[1]).toString();
		var parsedLog_matched = JSON.parse(jsonFile);
		exports.createTestFlow( parsedLog_detail, parsedLog_matched, fileName);
	}
	else{
		console.log("ERROR: Unknown command line input format");
	}
}
