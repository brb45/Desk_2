var fs 			= require('fs');
var path 		= require('path');	
var objectMerge = require('deepmerge');		// for merging the Prepare and Add maps to the input map
var readLine 	= require('readline');		// for reading the log file
var async		= require('async');			// for writing the files in parallel

// Keywords for creating the Summary
// We don't care about tests with these names in regards to creating the Summary
const summarySkipWords = ["parameters.INSERT_DUT", "INITIALIZE_DUT", "LOAD_PATH_LOSS_TABLE", "GLOBAL_SETTINGS", "CONNECT_IQ_TESTER", "DUT_SET_MODE", "DISCONNECT_IQ_TESTER", "REMOVE_DUT", "CAL"];

// We only care about these test items
const summaryRegex = /\.*FREQ\.*|ANT\d|\.*BANDWIDTH\.*|PACKET_FORMAT|MEASUREMENTS|STANDARD|DATA_RATE/;

// error codes ADD MORE PLEASE
// Error Codes < 0 mean couldn't parse
// Error Codes > 0 mean could parse, but might be incorrect results/non-breaking bugs
const ERROR_UNMATCHED_OUTPUTS =  1;		// MPS: Some outputs couldn't be matched to the appropriate input. Has no meaning with regards to the Web App
const ERROR_FILE_OPEN_ERR 	  = -1;		// Error opening the log file
const ERROR_INVALID_LOG_FILE  = -2;		// The passed in file is not a valid log file

//Global Constants
const FROM_PREPARE 		 	  = "prepare";
const FROM_ADD 	   		 	  = "add";
const FROM_ADD_MT  		 	  =	"MT"
const FROM_RUN 	   		 	  = "run";
const FROM_RUN_MT  		 	  = "runMT";
const FAIL_FUNCTION_ERROR	  = "Failed on function error";
const FAIL_LIMIT_ERROR   	  = "Failed on limits";
const NO_VALUE 			 	  = "NO_VALUE";

// create a class to hold all the parameters we use. These used to be global variables.
var parserParameters = function(){
	// for keeping our place in the file
	this.wholeblock   	   = [];	// Array containing each line of data
	this.i 			  	   = 0; 	// Line counter within the block
	this.blocklength  	   = 0;

	// for constructing the parameters.runlist summary. Basically just says which runs pass/fail.
	this.counter 		   = 1;     // run counter
	this.numberOfTestItem  = 0;
	this.PnumberOfTestItem = 0;
	this.runlist 		   = [];

	// these grab all the inputs and outputs
	// Only useful for MPS Runs
	// Basically, we need them to match the outputs in the TEST_RUN block to the correct inputs in the TEST_ADD block.
	this.inputParameters   = {};	// total inputs
	this.resultsDataMap    = {};	// output results, contains the matched inputs
	this.PrepareMap 	   = {};	// inputs from a test prepare block
	this.AddMap 		   = {};	// inputs from a test add block
	this.RunMap 		   = {};	// output results from a test run block
	this.AddMapMT 		   = {};	// inputs from an add MT block
	this.RunMapMT 		   = {};	// output results from a run MT block

	// Contains the details of the test errors, if we can find them
	this.returnErrorDetails 	   = {};
	this.returnErrorDetailKeywords = []; // Error Detail keywords

	// These grab every piece of data.
	// We don't attach the input to the output, so we only need 1 map.	
	this.resultsDataMapComplete	   = {};

	// these keep track of which test number we are on
	this.testIdAdd = "";	// The test ID of the most recent Add block (for matching inputs to outputs)
	this.testIdMT  = "";	// The test ID of the most recent MT Add block
	this.testId    = "";	// The test ID in general.

	// Records the max number of outputs for all the testIds.
	// For filling in NO_VALUE into the json files
	// They will be of form {testId: output#}, where output# specifies which output had the most outputs
	this.maxOutputSizeComplete = {};   
	this.maxOutputSize 		   = {};

	// store return values
	this.errStatus = {
		"error_code" : 0,
		"Chipset"    : NO_VALUE
	};

	// we store the test ID of the parameters.INSERT_DUT block so we can extract the Chipset name. This is important for the IQfact+ Log web app.
	this.INSERT_DUT = "";

	// Create the input summary file.
	this.summaryCount 		   = 0;		// Number of items in the parameters.summaryArray
	this.resultsDataMapSummary = {};	// The final object that we convert into a json file. Holds parameters.summaryArray, runList, parameters.summaryCount.
	this.summaryArray 		   = [];	// Array holding the different combination of inputs

	// Used for valid log file checking. Basically, if we get through the whole file and never recognize a block of data, the log file 
	// is invalid and we return ERROR_INVALID_LOG_FILE.
	this.matchFound = false;
}

var SetupVariables = function(){
	// Store the error detail keywords in an array to use for checking later.
	// Not used for the Web App
	var parameters = new parserParameters();
	if (fs.existsSync(__dirname + "/summarizeKeywords.txt")){
		var fileContents = fs.readFileSync(__dirname + "/summarizeKeywords.txt").toString().split('\n');
		for(var j = 0; j < fileContents.length; j++){
			var tempString = fileContents[j].replace(/\r/, "");
			tempString = tempString.trim();
			if(/\S/.test(tempString)){
				parameters.returnErrorDetailKeywords.push(tempString)
			}
		}
	}
	else {
		parameters.returnErrorDetailKeywords = [];
	}
	return parameters;
}

exports.fileparser = function(filePath, outputLocation, createJsonFiles, callback)
{
	var parameters = SetupVariables();

	if (fs.existsSync(filePath)) {
	    var lineReader = readLine.createInterface({
				input: fs.createReadStream(filePath)
			});

	    // Separate the log file into blocks.
		lineReader.on('line', function (line) {
			lineReader.pause()
			line = line.replace(/\s*\#.*\#\s*/, ""); // Get rid of the timestamps if they exist, of form #2017-11-22-33-44# 
			line = line.replace(/\r|\n|\r\n/gm, ""); //	Not sure if lineReader automatically removes line breakers, but just to be safe, try to replace anyways
			// RegExp is #.<ANYTHING>____
			if(/\d+\..*\_+\s*$/.test(line) || line.indexOf("----") != -1){
				parameters.blocklength = parameters.wholeblock.length;
				var parserAns = packedParser(parameters);
				if(parserAns){
					parameters.matchFound = true;
				}
				parameters.wholeblock = [];
				parameters.wholeblock.push(JSON.parse(JSON.stringify(line)));
			}
			else{
				parameters.wholeblock.push(JSON.parse(JSON.stringify(line)))
			}
			lineReader.resume();	
		});

		// We finished reading the file. 
		lineReader.on('close', function(){
			parameters.resultsDataMapSummary["table"]   = JSON.parse(JSON.stringify(parameters.summaryArray));
			parameters.resultsDataMapSummary["runlist"] = JSON.parse(JSON.stringify(parameters.runlist));
			parameters.resultsDataMapSummary["count"]   = parameters.summaryCount;

			// Valid log file and we are creating the json files
			if(createJsonFiles && parameters.matchFound){
				var writtenFileName = path.basename(filePath, path.extname(filePath));
				// write the four files in parallel. 
				async.parallel([
					function(callback){
						fs.writeFile(outputLocation + '/' + writtenFileName + '_matched.json', JSON.stringify(parameters.resultsDataMap), function(err){
							if(err){
								console.log(err);
							}
							else{
								console.log("Created " + writtenFileName + "_matched.json.");
							}
							callback(err, 'one');
						});
					},
					function(callback){
						fs.writeFile(outputLocation + '/' + writtenFileName + '_detail.json', JSON.stringify(parameters.resultsDataMapComplete), function(err){
							if(err){
								console.log(err);
							}
							else{
								console.log("Created " + writtenFileName + "_detail.json.");
							}
							callback(err, 'two');
						});
					},
					function(callback){
						fs.writeFile(outputLocation + '/' + writtenFileName + '_summary.json', JSON.stringify(parameters.resultsDataMapSummary), function(err){
							if(err){
								console.log(err);
							}
							else{
								console.log("Created " + writtenFileName + "_summary.json.");
							}
							callback(err, 'three');
						});
					},
					function(callback){
						fs.writeFile(outputLocation + '/' + writtenFileName + '_errors.json', JSON.stringify(parameters.returnErrorDetails), function(err){
							if(err){
								console.log(err);
							}
							else{
								console.log("Created " + writtenFileName + "_errors.json.");
							}
							callback(err, 'four');
						});
					}					
				],
				// once done writing the files, execute this callback function
				function(err){
					if(parameters.resultsDataMapComplete[parameters.INSERT_DUT] != null && parameters.resultsDataMapComplete[parameters.INSERT_DUT]["input"] != null && parameters.resultsDataMapComplete[parameters.INSERT_DUT]["input"]["DUT_DLL_FILENAME"] != null){
						var dllFileName = parameters.resultsDataMapComplete[parameters.INSERT_DUT]["input"]["DUT_DLL_FILENAME"];
						parameters.errStatus["Chipset"] = dllFileName.replace(/\.dll/, "");
					}
					if(err){
						console.log(err);
					}
					else{
						console.log("results: successful");
						console.log("Chipset: " + parameters.errStatus["Chipset"]);
					}
					if(callback && typeof callback == "function"){
						callback(JSON.parse(JSON.stringify(parameters.errStatus)), JSON.parse(JSON.stringify(parameters.resultsDataMapComplete)), JSON.parse(JSON.stringify(parameters.resultsDataMap)), JSON.parse(JSON.stringify(parameters.returnErrorDetails)));
					}
				});
				// Synchronous Version of above code
				// fs.writeFileSync(outputLocation + '/' + writtenFileName + '_matched.json', JSON.stringify(parameters.resultsDataMap));
				// console.log("Created " + writtenFileName + "_matched.json.");
				// fs.writeFileSync(outputLocation + '/' + writtenFileName + '_detail.json', JSON.stringify(parameters.resultsDataMapComplete));
				// console.log("Created " + writtenFileName + "_detail.json.");
				// fs.writeFileSync(outputLocation + '/' + writtenFileName + '_summary.json', JSON.stringify(parameters.resultsDataMapSummary));
				// console.log("Created " + writtenFileName + "_summary.json.");
				// fs.writeFileSync(outputLocation + '/' + writtenFileName + '_errors.json', JSON.stringify(parameters.returnErrorDetails));
				// console.log("Created " + writtenFileName + "_errors.json.");
				// console.log("Succesfull Parsing");
				// if(callback && typeof callback == "function"){
				// 	if(parameters.resultsDataMapComplete[parameters.INSERT_DUT] != null && parameters.resultsDataMapComplete[parameters.INSERT_DUT]["input"] != null && parameters.resultsDataMapComplete[parameters.INSERT_DUT]["input"]["DUT_DLL_FILENAME"] != null){
				// 		var dllFileName = parameters.resultsDataMapComplete[parameters.INSERT_DUT]["input"]["DUT_DLL_FILENAME"];
				// 		parameters.errStatus["Chipset"] = dllFileName.replace(/\.dll/, "");
				// 	}
				// 	callback(parameters.errStatus, JSON.parse(JSON.stringify(parameters.resultsDataMapComplete)), JSON.parse(JSON.stringify(parameters.resultsDataMap)), JSON.parse(JSON.stringify(parameters.returnErrorDetails)));
				// }
			}
			// Otherwise we aren't creating the JSON files, so just do the callback
			else {
				if(!parameters.matchFound){
					console.log("ERROR: INVALID LOG FILE");
					parameters.errStatus["error_code"] = ERROR_INVALID_LOG_FILE;
				}
				if(callback && typeof callback == "function"){
					if(parameters.resultsDataMapComplete[parameters.INSERT_DUT] != null && parameters.resultsDataMapComplete[parameters.INSERT_DUT]["input"] != null && parameters.resultsDataMapComplete[parameters.INSERT_DUT]["input"]["DUT_DLL_FILENAME"] != null){
						var dllFileName = parameters.resultsDataMapComplete[parameters.INSERT_DUT]["input"]["DUT_DLL_FILENAME"];
						parameters.errStatus["Chipset"] = dllFileName.replace(/\.dll/, "");
					}
					callback(JSON.parse(JSON.stringify(parameters.errStatus)), JSON.parse(JSON.stringify(parameters.resultsDataMapComplete)), JSON.parse(JSON.stringify(parameters.resultsDataMap)), JSON.parse(JSON.stringify(parameters.returnErrorDetails)));
				}
			}
			// global.gc();
		});
	}
	else{
		console.log("ERROR: COULD NOT OPEN FILE");
		parameters.errStatus["error_code"] = ERROR_FILE_OPEN_ERR;
		if(callback && typeof callback == "function"){
			callback(JSON.parse(JSON.stringify(parameters.errStatus)), JSON.parse(JSON.stringify(parameters.resultsDataMapComplete)), JSON.parse(JSON.stringify(parameters.resultsDataMap)), JSON.parse(JSON.stringify(parameters.returnErrorDetails)));
		}
	}	
}

// Determines which kind of block we're dealing with. If we can't figure it out, then return false.
var packedParser = function(parameters)
{	
	parameters.i = 0;
	var sCurrentLine = "";
	//we enumerate across the block
	for(;parameters.i < parameters.blocklength; parameters.i++)
	{
		sCurrentLine = JSON.parse(JSON.stringify(parameters.wholeblock[parameters.i]));

		// MPS test
		if( /\d+\..*TEST_PREPARE.*\_+\s*$/.test(sCurrentLine) ||
			/\d+\..*TEST_ADD.*\_+\s*$/.test(sCurrentLine)     ||
			/\d+\..*TEST_RUN.*\_+\s*$/.test(sCurrentLine) ){
			perMPSBlock(parameters);
			return true;
		}

		// Not an MPS test, so just go through it and parse normally
		else if(/^\d+\..*\_+\s*$/.test(sCurrentLine)){
			// console.log("NonMps");
			parameters.testId = sCurrentLine.trim().replace(/\s*\_+$/, ""); 	// Remove trailing "____"
			parameters.testIdAdd = parameters.testId;
			if(parameters.testId.indexOf("INSERT_DUT") != -1){
				parameters.INSERT_DUT = parameters.testId;
			}
			perNotMPSBlock(parameters);
			return true;
		}

		// End of run. Parse the summary in lastStep() and skip to end of summary.
		else if(sCurrentLine.indexOf("P A S S") != -1 || sCurrentLine.indexOf("F A I L") != -1){
			//console.log("End Of Run");
			var status = "pass";
			if(sCurrentLine.indexOf("F A I L") != -1){
				status = "fail";
			}
			// console.log(parameters.counter);
			lastStep(parameters, status);
			return true;
		}
	}
	return false;
}

var perMPSBlock = function(parameters)
{
	var sCurrentLine = "";
	// MPS has 3 parts: Prepare, Add, and a Run block. Figure out which block we are working on, and run the specific process.
	for(;parameters.i < parameters.blocklength; parameters.i++){
		sCurrentLine = JSON.parse(JSON.stringify(parameters.wholeblock[parameters.i]));
		if(sCurrentLine.indexOf("TEST_PREPARE") != -1){
			//console.log("--MPS Prepare in");
			parameters.testId = sCurrentLine.trim().replace(/\s*_+$/, "");  
			processPrepare(parameters);
			//console.log("--MPS Prepare out");
			return;
		}

		if(sCurrentLine.indexOf("TEST_ADD") != -1){
			//console.log("--MPS Add in");
			parameters.testId = sCurrentLine.trim().replace(/\s*_+$/, "");
			if(sCurrentLine.indexOf("MT_") != -1){
				processAdd(parameters, FROM_ADD_MT);
			}
			else{
				processAdd(parameters);				
			}

			//console.log("--MPS Add out");
			return;
		}

		if(sCurrentLine.indexOf("TEST_RUN") != -1){
			//console.log("--MPS Run in");
			parameters.testId = sCurrentLine.trim().replace(/\s*_+$/, ""); 
			var runAns = processRun(parameters);
			//console.log("--MPS Run out");
			if(runAns != 0){
				// console.log("Run process no output")
			}
			return;
		}
	}
}

// MPS: processes a TEST_PREPARE block
var processPrepare = function(parameters)
{
	// Store all the data for this MPS test into an object parameters.PrepareMap. We later combine this with parameters.AddMap
	// to finally store the data in resultsData, which turns into a .json file
	parameters.PrepareMap = {};
	var inputFlag = true;
	var sCurrentLine = "";
	for(;parameters.i < parameters.blocklength; parameters.i++)
	{
		sCurrentLine = JSON.parse(JSON.stringify(parameters.wholeblock[parameters.i]));
		if(sCurrentLine.indexOf("Test Time =") != -1){
			inputFlag = false;
			continue;
		}
		var matchAns = performInputMatch(parameters, sCurrentLine, FROM_PREPARE, inputFlag); // if there is a match, this will also add the relevant data into the Map

		// Valid input, continue to the next line 
		if(matchAns == 0){
			continue;
		}
		else if(matchAns == -1){
			//console.log("No Match");
		}		
	}
}

// MPS: processes a TEST_ADD block
var processAdd = function(parameters, from = FROM_ADD)
{

	// Store all the data for this MPS test into an object parameters.AddMap. We later combine this with parameters.PrepareMap
	// to finally store the data in parameters.resultsDataMap which turns into a .json file 
  	var inputFlag = true;
  	var sCurrentLine = JSON.parse(JSON.stringify(parameters.wholeblock[parameters.i]));
	if(from == FROM_ADD){
		parameters.AddMap = {};
		parameters.testIdAdd = sCurrentLine.trim().replace(/\s_+$/, "");  	
	}
	else if(from == FROM_ADD_MT){
		parameters.AddMapMT = {};
		parameters.testIdMT = sCurrentLine.trim().replace(/\s+_+$/, "");  
	}
	for(;parameters.i < parameters.blocklength;parameters.i++)
	{
		sCurrentLine = JSON.parse(JSON.stringify(parameters.wholeblock[parameters.i]));
		if(sCurrentLine.indexOf("Test Time =") != -1){
			inputFlag = false;
			continue;
		}
		var matchAns = performInputMatch(parameters, sCurrentLine, from, inputFlag); // if there is a match, this will also add the relevant data into the Map
		// Valid input, continue to the next line 
		if(matchAns == 0){
			continue;
		}
		else if(matchAns == -1){
			//console.log("No Match");
		}
	}
	mergeToinputParameters(parameters, from);
}

// MPS: processes a TEST_RUN block
var processRun = function(parameters)
{
	parameters.RunMap = {};
	parameters.RunMapMT = {};
	var sCurrentLine = "";
	// skip to the results
	var skipAns = skipToResults(parameters);
	if (skipAns == -1){	// Hit Skip/Error message
		sCurrentLine = JSON.parse(JSON.stringify(parameters.wholeblock[parameters.i]));
		addErrorStatus(parameters, sCurrentLine);
		return -1;
	}
	else if(skipAns == -2){	// Hit end of block
		return -1;
	}

	for(;parameters.i < parameters.blocklength;parameters.i++){
		sCurrentLine = JSON.parse(JSON.stringify(parameters.wholeblock[parameters.i]));
		var matchAns = performOutputMatch(parameters, sCurrentLine);    //process and store output data
		if(matchAns == 0){
			continue;
		}
		else if(matchAns == -1){
			//console.log("No Match");
		}
	}
	addToResults(parameters);
	clearMaps(parameters);
	return 0;
}

var perNotMPSBlock = function(parameters)
{
	var tempNonMPSinputParameters = {}; 
	// inputFlag signifies if we're before or after "Test Time =", since we assume everything after that is a output line
	var inputFlag = true;
	// inputBlock signifies if we're in the block of text where all the inputs are. All the inputs are stuck together, so as soon as
	// we hit an invalid input line we stop accepting inputs. This is important because sometimes the junk lines between the inputs and outputs
	// look like valid lines but aren't.
	var inputBlock = true;
	var sCurrentLine = "";
	parameters.i++;
	for(;parameters.i < parameters.blocklength;parameters.i++){
		sCurrentLine = JSON.parse(JSON.stringify(parameters.wholeblock[parameters.i]));
		//check for skipped test
		if((sCurrentLine.indexOf("Skipped") != -1 && sCurrentLine.indexOf('[') == -1) || 
			sCurrentLine.indexOf("Skipped by") != -1){
			addToCompleteMap(parameters, "STATUS", sCurrentLine, "output", parameters.testId, "noLimits");
			break;
		}
		if(/^\s/.test(sCurrentLine)){
			continue;
		}
		var afterParsed = sCurrentLine.split(':');
		if(sCurrentLine.indexOf("Test Time =") != -1){
			inputFlag = false;
			continue;
		}
		if(inputFlag){
			// all the inputs should be in one big block. Soon as an invalid inputs is found, 
			// we stop adding inputs
			if(validInputLine(sCurrentLine) && inputBlock){
				var key   = afterParsed[0];
				var value = afterParsed.slice(1).join(':');
				key = key.trim();
				value = value.trim();
				addToCompleteMap(parameters, key, value, "input", parameters.testId, "noLimits");
				tempNonMPSinputParameters[key] = value;
			}
			else{
				inputBlock = false;
			}
		}
		else{ // we assume everything after Test Time is an output
			if(afterParsed.length<2){
				continue;
			}
			else if(/^\s*---\s*\[Failed\].*/.test(sCurrentLine)){
				continue;
			}
			else{
				var key = afterParsed[0].trim();
				var value = afterParsed.slice(1).join(':').trim();
				var k = /\((\s*\-?\d*\.?\d*\s*),(\s*\-?\d*\.?\d*\s*)\)/;	// Matches ( limits[1] , limits[2] ),
				var limits = sCurrentLine.match(k);
				var lowerLimit;
				var upperLimit;

				// Limits Exist, so extract them
				if(limits != null){
					lowerLimit = limits[1].trim();
					upperLimit = limits[2].trim();
					value = value.replace(k, "").trim();	// get rid of "( , )"in the line
					value = value.replace(/[ ]{1,}/, ' ');  // replace multiple spaces with single space
					if (sCurrentLine.trim().endsWith("--- [Failed]")){	// Failed on limit error, only possible when limits exist
						addToCompleteMap(parameters, "STATUS", FAIL_LIMIT_ERROR, "output", parameters.testId, "noLimits");
					}
				}
				// No limits
				else{
					lowerLimit = "noLimits";
				}
				addToCompleteMap(parameters, key, value, "output", parameters.testId, lowerLimit, upperLimit);

				// Check the error message for test function failure. We don't use addErrorMessage because we just add to the complete map, not the matched map.
				if(sCurrentLine.indexOf("ERROR_MESSAGE") != -1 && sCurrentLine.indexOf(':') != -1){
					var errorMessage = sCurrentLine.split(':')[1];

					if ((/\S/.test(errorMessage)) && (errorMessage.indexOf("Function completed") == -1)){
						addToCompleteMap(parameters, "STATUS", FAIL_FUNCTION_ERROR, "output", parameters.testId, "noLimits");
					}
					// if the ERROR_MESSAGE is blank, then look ahead a couple of lines to see if the test failed signified by "--- [Failed] :"
					else if (!(/\S/.test(errorMessage))) {
						for(var j = parameters.i; j < parameters.blocklength && j < parameters.i + 5; j++){
							if(/\-\-\-\s*\[Failed\]\s*\:/.test(parameters.wholeblock[j])){
								addToCompleteMap(parameters, "STATUS", FAIL_FUNCTION_ERROR, "output", parameters.testId, "noLimits");
								addToCompleteMap(parameters, "ERROR_MESSAGE", parameters.wholeblock[j].trim(), "output", parameters.testId, "noLimits");
								parameters.wholeblock[j] = "";
								break;
							}
						}
					}
				}
			}
		}
	}
	if(!isEmpty(tempNonMPSinputParameters)){
		var flag = true;
		for(var j = 0; j < summarySkipWords.length; j++){
			if(parameters.testId.indexOf(summarySkipWords[j]) != -1){
				flag = false;
				break;
			}
		}
		if(flag){
			var potentialMap = extractInputSummary(parameters, tempNonMPSinputParameters);
			if(potentialMap != -1){
				parameters.summaryArray.push(potentialMap);
				parameters.summaryCount++;
			}
		}
	}
	addToCompleteMap(parameters, "index", "output" + parameters.counter.toString(), "output", parameters.testId, "noLimits");
	return -1;
}

// process the end summary block
var lastStep = function(parameters, result)
{
	var runid = parameters.counter;
	console.log("Finished Run " + parameters.counter.toString());
	parameters.counter++;
	var sCurrentLine = "";
	for(;parameters.i < parameters.blocklength; parameters.i++) {
		sCurrentLine = JSON.parse(JSON.stringify(parameters.wholeblock[parameters.i]));
		if((isNaN(sCurrentLine.charAt(0)) == false) && (sCurrentLine.charAt(0) != ' ') && (sCurrentLine.charAt(0) != ' ')){
			var list = sCurrentLine.split('.');
			parameters.numberOfTestItem = parseInt(list[0]);
		}
		if(sCurrentLine.indexOf("-------------------------------------------------------------------") != -1){
			break;
		}
	}
	if(parameters.counter == 2){
		parameters.PnumberOfTestItem = parameters.numberOfTestItem;
	}
	if(parameters.numberOfTestItem != parameters.PnumberOfTestItem){
		console.log("different number of test items in run " + (parameters.counter-1)) ;
	}
	parameters.PnumberOfTestItem = parameters.numberOfTestItem;
	var run = {};
	run['id'] = runid;
	run['result'] = result;
	parameters.runlist.push(run);
}

// Put the current line to the correct maps.
var performInputMatch = function(parameters, sCurrentLine, from, inputFlag)
{	
	if(errorOrSkipMessage(sCurrentLine)){
		addErrorStatus(parameters, sCurrentLine);
	}

	if(!inputFlag){
		return 0;
	}

	else if(validInputLine(sCurrentLine) == 1){
		var afterParsed = sCurrentLine.split(':');
		var key = afterParsed[0].trim();
		var value = afterParsed[1].trim();

		addValueToMap(parameters, key, value, from);
		addToCompleteMap(parameters, key, value, "input", parameters.testId);
		return 0;
	}
	return -1;
}

var performOutputMatch = function(parameters, sCurrentLine)
{
	if(errorOrSkipMessage(sCurrentLine)){
		addErrorStatus(parameters, sCurrentLine);
		return 0;
	}

	if(validOutputLine(sCurrentLine) == 1){ // has an ( , ) in it, so is a valid output line

		// Output line can look like <TEST_ITEM_NAME>		: 			<value>     <units>   (lowerLimit, upperLimit)
		var afterParsed = sCurrentLine.split(':');
		var value = afterParsed.slice(1).join(':').trim();
		var k = /\((\s*\-?\d*\.?\d*\s*),(\s*\-?\d*\.?\d*\s*)\)/;	// Matches ( limits[1] , limits[2] ),
		var limits = sCurrentLine.match(k);
		var lowerLimit;
		var upperLimit;

		var failureMessage = "Passed";
		var failFlag = false;
		
		// Limits Exist, so extract them
		if(limits != null){
			lowerLimit = limits[1].trim();
			upperLimit = limits[2].trim();
			value = value.replace(k, "").trim();	// get rid of "( , )"in the line and removing trailing whitespace
			value = value.replace(/[ ]{1,}/, ' ');  // replace multiple spaces with single space
			if (sCurrentLine.trim().endsWith("--- [Failed]")){	// Failed on limit error, only possible when limits exist
				failureMessage = FAIL_LIMIT_ERROR
				failFlag = true;
			}
		}
		else{// Should not happen ever
			console.log("ERROR: Unable to find limits for:", sCurrentLine);
		}


		// If the units don't exist, when we split on white space, then the units field will be "(lowerlimit,", so we just check if the '(' is there
		// if(units.indexOf('(') != -1){
		// 	units = "";
		// }

		// var valueUnits = (value + ' ' + units).trim();

		// Grab the lower and upper limits
		// RegExp finds (lowerLimit , upperLimit)
		// var k = /\((\s*\-?\d*\.?\d*\s*),(\s*\-?\d*\.?\d*\s*)\)/;
		// var limits = sCurrentLine.match(k);
		// var lowerLimit = limits[1].trim();
		// var upperLimit = limits[2].trim();

		// add to normal map
		// MPS output line
		var keyword = "";
		keyword = afterParsed[0].trim();
		if(/\.\d{3}\./.test(sCurrentLine)) {
			var type = "";
			var testIdTemp = determineTestId(parameters, keyword);
			if(testIdTemp == -1){
				console.log("ERROR: COULDN'T MATCH INPUT TO OUTPUT FOR", sCurrentLine)
				console.log(parameters.testId);
				parameters.errStatus["error_code"] = ERROR_UNMATCHED_OUTPUTS;	// Doesn't affect Web App usage, so not completely breaking.
			}

			if(sCurrentLine.indexOf("MT_") != -1){	// MT output, store to MT map
				type = FROM_RUN_MT;
				// testIdTemp = parameters.testIdMT;
			}
			else{
				type = FROM_RUN;
				// testIdTemp = parameters.testIdAdd;
			}
			addValueToMap(parameters, keyword, value, type, failureMessage, failFlag, testIdTemp, lowerLimit, upperLimit);
		}
		// non MPS output line, possible error (but probably not)
		else{
		// 	keyword = afterParsed[0].trim();
		// 	addValueToMap(keyword, valueUnits, FROM_RUN, failureMessage, failFlag, parameters.testId, lowerLimit, upperLimit);
			// console.log("POSSIBLE ERROR: Found Possible NON-MPS output line in MPS block, Test ID = " + parameters.testId);
			// console.log(sCurrentLine);		
		}

		// Add to the complete map regardless
		addToCompleteMap(parameters, keyword, value, "output", parameters.testId, lowerLimit, upperLimit);
		if(failFlag){
			addToCompleteMap(parameters, "STATUS", FAIL_LIMIT_ERROR, "output", parameters.testId, "noLimits");
		}
		return 0;
	}
	return -1;
}

// checks either the block's ERROR_MESSAGE to see if the test failed on function error
// or if the test item was skipped. Store the outcome in the STATUS field.
var addErrorStatus = function(parameters, sCurrentLine)
{
	var failFlag = false;
	// Interpreting ERROR_MESSAGE
	if(sCurrentLine.indexOf("ERROR_MESSAGE") != -1 && sCurrentLine.indexOf(':') != -1){
		var errorMessage = sCurrentLine.split(':')[1];
		errorMessage = errorMessage.trim();
		var failureMessage = "Passed";
		if ((/\S/.test(errorMessage)) && (errorMessage.indexOf("Function completed") == -1)){
			failFlag = true;
			failureMessage = FAIL_FUNCTION_ERROR;
		}
		// if no errorMessage
		else if (!(/\S/.test(errorMessage))) {
			// Look ahead for "--- [Failed] :"
			for(var j = parameters.i; j < parameters.blocklength && j < parameters.i + 5; j++){
				if(/\-\-\-\s*\[Failed\]\s*\:/.test(parameters.wholeblock[j])){
					failFlag = true;
					failureMessage = FAIL_FUNCTION_ERROR;
					errorMessage = parameters.wholeblock[j].trim();
					break;
				}
			}
		}
		for(var testIdTemp in parameters.inputParameters){
			addValueToMap(parameters, "ERROR_MESSAGE", errorMessage, FROM_RUN, failureMessage, failFlag, testIdTemp, "", "");
			addValueToMap(parameters, "ERROR_MESSAGE", errorMessage, FROM_RUN_MT, failureMessage, failFlag, testIdTemp, "", "");		
		}

		addToCompleteMap(parameters, "ERROR_MESSAGE", errorMessage, "output", parameters.testId, "noLimits");
		if(failFlag){
			addToCompleteMap(parameters, "STATUS", FAIL_FUNCTION_ERROR, "output", parameters.testId, "noLimits");
		}
	}
	// Interpreting Skip message
	else if( ((sCurrentLine.indexOf("Skipped by") != -1 ) ||
		   ( (sCurrentLine.indexOf("Skipped") != -1) && (sCurrentLine.indexOf('[') == -1))) ){
		addToCompleteMap(parameters, "STATUS", sCurrentLine.trim(), "output", parameters.testId, "noLimits");
		addToCompleteMap(parameters, "ERROR_MESSAGE", NO_VALUE, "output", parameters.testId, "noLimits");
	}

	addToCompleteMap(parameters, "index", "output" + parameters.counter.toString(), "output", parameters.testId, "noLimits");
}

// Simply adds the key value pair to the specified map. 
var addValueToMap = function(parameters, key, value, from, failureMessage, failFlag, testIdTemp, lowerLimit, upperLimit)
{
	if(from == FROM_PREPARE){
		parameters.PrepareMap[key] = value;
	}
	else if(from == FROM_ADD){
		parameters.AddMap[key] = value;
	}
	else if(from == FROM_ADD_MT){
		parameters.AddMapMT[key] = value;
	}
	else {
		var tempMap = {};
		if(from == FROM_RUN){
			tempMap = parameters.RunMap;
		}
		else if(from == FROM_RUN_MT){
			tempMap = parameters.RunMapMT;
		}
		if(tempMap[testIdTemp] == null){
			tempMap[testIdTemp] = {};
			tempMap[testIdTemp]["STATUS"] = "Passed";
		}
		tempMap[testIdTemp][key] = [value, lowerLimit, upperLimit];
		if(failFlag){
			tempMap[testIdTemp]["STATUS"] = failureMessage;
		}
	}
}

// merge the prepare map and add/MT maps into the input maps
var mergeToinputParameters = function(parameters, from)
{
	var testIdMap = {};
	if(from == FROM_ADD){
		parameters.inputParameters[parameters.testIdAdd] = objectMerge(parameters.PrepareMap, parameters.AddMap);
		testIdMap = parameters.inputParameters[parameters.testIdAdd];
	}

	else if(from == FROM_ADD_MT){
		parameters.inputParameters[parameters.testIdMT] = objectMerge(parameters.PrepareMap, parameters.AddMapMT);
		testIdMap = parameters.inputParameters[parameters.testIdMT];
	}
	if(!isEmpty(testIdMap)){
		var potentialMap = extractInputSummary(parameters, testIdMap);
		if(potentialMap != -1){
			parameters.summaryArray.push(potentialMap);
			parameters.summaryCount++;
		}
	}
}

// Extract the summary inputs from the results. 
var extractInputSummary = function(parameters, testIdMap){
	var tempMap = {};
	for(var testItem in testIdMap){
		if(summaryRegex.test(testItem)){
			tempMap[testItem] = testIdMap[testItem];
		}
	}
	if(isEmpty(tempMap)){
		return -1;
	}

	// make sure this combination of inputs hasn't been already added
	var repeatFlag = false;
	for(var j = 0; j < parameters.summaryArray.length; j++){
		var repeatFlagInner = true;
		for(var testItem in parameters.summaryArray[j]){
			if(tempMap[testItem] == null || parameters.summaryArray[j][testItem] != tempMap[testItem]){
				repeatFlagInner = false;
				break;
			}
		}
		if(repeatFlagInner){
			repeatFlag = true;
			break;
		}
	}
	if(!repeatFlag){	// not repeated
		return tempMap;
	}
	else{				// repeated
		return -1;
	}

}

// add the input Maps and Run Maps into the results Data Maps according to the test ID,
var addToResults = function(parameters)
{	
	var outputNum = "output" + parameters.counter.toString();
	for (var testIdTemp in parameters.inputParameters) {
		if (!parameters.inputParameters.hasOwnProperty(testIdTemp)) {
			continue;
		}
		if(parameters.resultsDataMap[testIdTemp] == null){
			parameters.resultsDataMap[testIdTemp] = {};
			parameters.resultsDataMap[testIdTemp]["input"] = parameters.inputParameters[testIdTemp]; 
		}
		if(parameters.RunMap[testIdTemp] != null){ //results in Run Map
			parameters.resultsDataMap[testIdTemp][outputNum] = parameters.RunMap[testIdTemp];
		}
		else if (parameters.RunMapMT[testIdTemp] != null){	//results in MT map
			parameters.resultsDataMap[testIdTemp][outputNum] = parameters.RunMapMT[testIdTemp];
		}
		else{
			console.log("ERROR: Results to the corresponding inputs not found!");
			console.log(testIdTemp);
		}
		var tempMap = parameters.resultsDataMap[testIdTemp];

		// Sometimes, especially on test function errors, the same test item will have a different number of items depending on the run.
		// To make it easier to tabulate, we fill the values that don't exist with NO_VALUE.
		fillWithNoValue(tempMap, parameters.maxOutputSize, testIdTemp, outputNum);
	}
}

var addToCompleteMap = function(parameters, key, value, from, testId, lowerLimit, upperLimit)
{
	var tempMap;
	if(parameters.resultsDataMapComplete[parameters.testId] == null){
		parameters.resultsDataMapComplete[parameters.testId] = {};
	}
	tempMap = parameters.resultsDataMapComplete[parameters.testId];
	if(from == "input"){
		if(tempMap["input"] == null){
			tempMap["input"] = {};
		}
		tempMap["input"][key] = value;
	}
	else if(from == "output"){
		var outputNum = "output" + parameters.counter.toString();

		if( tempMap[outputNum] == null){
			tempMap[outputNum] = {};
			tempMap[outputNum]["index"] = outputNum;
			tempMap[outputNum]["STATUS"] = "Passed";
		}
		if(lowerLimit == "noLimits"){
			tempMap[outputNum][key] = value;
		}
		else{
			tempMap[outputNum][key] = [value, lowerLimit, upperLimit];
		}

		if(key == "index"){
			// Sometimes, especially on test function errors, the same test item will have a different number of items depending on the run.
			// To make it easier to tabulate, we fill the values that don't exist with NO_VALUE.
			// We use the "index" keyword to trigger the check since we know it already always exists for each entry(added on creation), so we won't add anything, and it's always a specific value
			fillWithNoValue(tempMap, parameters.maxOutputSizeComplete, parameters.testId, outputNum);

			// Now, we try to check for specific errors. If the STATUS is failed on function error, we parse the block again and look for specific
			// keywords specified in the returnErrorDetailsKeywords array.
			if(tempMap[outputNum]["STATUS"] == FAIL_FUNCTION_ERROR){
				var tempLine = "";
				for(var j = 0; j < parameters.blocklength; j++){
					tempLine = parameters.wholeblock[j];
					for(var k = 0; k < parameters.returnErrorDetailKeywords.length; k++){
						if(tempLine.indexOf(parameters.returnErrorDetailKeywords[k]) != -1){
							if(parameters.returnErrorDetails[parameters.testId] == null){
								parameters.returnErrorDetails[parameters.testId] = {};
							}
							var tempMap = {};
							tempMap[outputNum] = tempLine;
							parameters.returnErrorDetails[parameters.testId] = tempMap;
						}
					}
				}
			}
		}
	}
}

// Fill the map specified by tempMap with NO_VALUE as needed
// HOWEVER, since we base of need from the number of parameters the map contains, not the contents,
// if for some magical reason the same test item has the same number of items but different items,
// this won't catch it. Should not be a problem though since this should be impossible.
var fillWithNoValue = function(tempMap, maxSize, testId, outputNum){
	if(maxSize[testId] == null){
		maxSize[testId] = outputNum; 
	}

	// The current number of outputs is larger than previous runs, so we have to fill the previous runs with NO_VALUE
	else if(numberOfProperties(tempMap[outputNum]) > numberOfProperties(tempMap[maxSize[testId]])){
		maxSize[testId] = outputNum;
		for(var outputNumTemp in tempMap){
			if(outputNumTemp == outputNum){
				continue;
			}
			else if(outputNumTemp == "input"){
				continue;
			}
			for(var property in tempMap[outputNum]){
				if(!tempMap[outputNumTemp].hasOwnProperty(property)){
					tempMap[outputNumTemp][property] = [NO_VALUE,"",""];
				}
			}
		}
	}

	// The current number of outputs is smaller than in previous runs, so we fill this run with NO_VALUE
	else if(numberOfProperties(tempMap[outputNum]) < numberOfProperties(tempMap[maxSize[testId]])){
		var maxOutput = maxSize[testId];
		for(var property in tempMap[maxOutput]){
			if(!tempMap[outputNum].hasOwnProperty(property)){
				tempMap[outputNum][property] = [NO_VALUE,"",""];
			}
		}
	}
}

// This tries to determine the test ID from the output line. 
// Called testItemName since it's just the name of the test item, not including the value
var determineTestId = function(parameters, testItemName)
{
	// the parts that we look for
	var packetFormat = "";
	var bandwidth    = "";
	var dataRate     = "";
	var measurement  = "";
	var testName     = "";
	var testType	 = "";
	var powerLevel   = "";
	if(testItemName.indexOf('@') != -1){
		powerLevel   = parseFloat(testItemName.split('@')[1]);
	}
	var iDNum;

	// NOTE:
	// Test name will be of form of something like 1)VHT20_MCS0.PER_MAX.000.ACK_COUNT.@-20.00
	//											or 2)      MCS0.PER_MAX.000.ACK_COUNT.@-20.00 if NON-HT packet format
	// In this case, VHT is packet format
	// 20 is the bandwidth BW-20
	// MCS0 is the data rate
	// PER_MAX is the measurement
	// 000 is the ID number (for multiple tests of the same name)
	// -20 is the power level

	// Extract the parts
	// Grab the packet format, bandwidth, and data rate
	var parts = testItemName.split('.');
	if(parts[0].indexOf('_') == -1){
		packetFormat = "NON_HT";
		bandwidth = "";
		dataRate = parts[0]
	}
	else{
		var tempParts = parts[0].split('_');
		dataRate = tempParts[1];
		for(var j = 0; j < tempParts[0].length; j++){
			if(!isNumber(tempParts[0][j])){
				packetFormat += tempParts[0][j];
			}
			else{
				break;
			}
		}
		bandwidth = "BW-" + tempParts[0].substring(j, tempParts[0].length);
	}
	if(packetFormat == "HT"){
		packetFormat = "HT_MF";
	}

	// Determine the measurement
	measurement = parts[1];
	iDNum = parseInt(parts[2]);
	testName = parts[3];

	if(measurement.indexOf("EVM") 			 != -1){
		testType = 'TX';
		measurement = 'E';
	}
	else if(measurement.indexOf("PER_SENS")  != -1){
		testType = 'RX';
		measurement = 'L';
	}
	else if(measurement.indexOf("SPECTRUM")  != -1){
		testType = 'TX';
		measurement = 'S';
	}
	else if(measurement.indexOf("PER_SWEEP") != -1){
		testType = 'RX';
		measurement = 'S';
	}
	else if(measurement.indexOf("MASK") 	 != -1){
		testType = 'TX';
		measurement = 'M';
	}
	else if(measurement.indexOf("PER_MAX") 	 != -1){
		testType = 'RX';
		measurement = 'H'; // can also be I if MT test
	}
	else if(measurement.indexOf("POWER") 	 != -1){
		testType = 'TX';
		measurement = 'P';
	}
	else if(measurement.indexOf("RAMP") 	 != -1){
		testType = 'TX';
		measurement = 'R';
	}	
	else{
		console.log("ERROR: Unknown Measurement Type: " + measurement);
	}

	// try to find the corresponding test ID
	var potentialIds = [];
	var MTFlagOutput = (testItemName.indexOf("MT_") == -1);
	for(var testIdTemp in parameters.inputParameters){
		var MTFlagInput = (testIdTemp.indexOf("MT_") == -1);
		var testMode;
		// Make sure if the output line is MT, we are looking at a MT test, or the inverse
		if(MTFlagOutput != MTFlagInput){
			continue;
		}

		if(testIdTemp.indexOf('TX') != -1 || parameters.inputParameters[testIdTemp]["MT_MODE"] == 'TX'){
			testMode = 'TX';
			// power level is just a number, so we have to get rid of the units before we check the match

			if( parameters.inputParameters[testIdTemp]["TX_POWER_DBM"] 		   != null && parseFloat(parameters.inputParameters[testIdTemp]["TX_POWER_DBM"].replace(/[a-zA-Z]*/, "" )) != powerLevel && 
				parameters.inputParameters[testIdTemp]["TARGET_POWER_DBM"] 	   != null && parseFloat(parameters.inputParameters[testIdTemp]["TARGET_POWER_DBM"].replace(/[a-zA-Z]*/, "" )) != powerLevel &&
				parameters.inputParameters[testIdTemp]["OPENLOOP_POWER_INDEX"] != null && parseFloat(parameters.inputParameters[testIdTemp]["OPENLOOP_POWER_INDEX"].replace(/[a-zA-Z]*/, "" )) != powerLevel){
				continue;
			}
		}
		else{
			testMode = 'RX';
		}

		// Make sure if the output line is TX, we are looking at a TX test, or RX to RX
		if(testMode != testType){
			continue;
		}
		// actually match the test ID.
		if( (parameters.inputParameters[testIdTemp]["PACKET_FORMAT"] == packetFormat) &&
			(parameters.inputParameters[testIdTemp]["DATA_RATE"] 	 == dataRate    ) ){
			if(packetFormat != "NON_HT"){
				if(parameters.inputParameters[testIdTemp]["BSS_BANDWIDTH"].indexOf(bandwidth) == -1 ){
					continue;
				}
			}
			if( (measurement == 'H') &&
			  	( (parameters.inputParameters[testIdTemp]["MEASUREMENTS"].indexOf('I') != -1) || 
				  (parameters.inputParameters[testIdTemp]["MEASUREMENTS"].indexOf('H') != -1) )) {
				//console.log("Matched", sCurrentLine, "to", testIdTemp);
				potentialIds.push(testIdTemp);
				// return testIdTemp;
			}
			else if (parameters.inputParameters[testIdTemp]["MEASUREMENTS"].indexOf(measurement) != -1){
				//console.log("Matched", sCurrentLine, "to", testIdTemp);
				potentialIds.push(testIdTemp);
				// return testIdTemp;
			}
		}
	}

	// if there's only one matching case, then return the only matching case
	if(potentialIds.length == 1){
		return potentialIds[0];
	}

	// PER_SWEEP special case
	// Just make sure the power level is within the stop and start levels.
	else if(measurement == 'S' && testType == 'RX'){
		for(var j = 0; j < potentialIds.length; j++){
			var startDB = parseFloat(parameters.inputParameters[potentialIds[j]]["START_POWER_LEVEL_DBM"]);
			var stopDB  = parseFloat(parameters.inputParameters[potentialIds[j]]["STOP_POWER_LEVEL_DBM"]);
			if(stopDB <= startDB){
				if(powerLevel >= stopDB && powerLevel <= startDB){
					return potentialIds[j];
				}
			}
			else{
				if(powerLevel <= stopDB && powerLevel >= startDB){
					return potentialIds[j];
				}
			}
		}
	}

	// the ID number will refer to the order in which the TEST_ADD blocks appear.
	else if(potentialIds.length > 1 && iDNum > 0){
		return potentialIds[iDNum];
	}
	// console.log(potentialIds);
	// console.log(packetFormat, bandwidth, dataRate, measurement, iDNum, testName, testType, powerLevel);
	
	// Error: no match
	return -1;
}

// moves i to the start of the output results
var skipToResults = function(parameters)
{
	var sCurrentLine = "";
	for(;parameters.i < parameters.blocklength ; parameters.i++){
		sCurrentLine = JSON.parse(JSON.stringify(parameters.wholeblock[parameters.i]));
		if( errorOrSkipMessage(sCurrentLine)){
			return -1;
		}
		if(sCurrentLine.indexOf("Test Time =") != -1){
			return 0;
		}
	}
	return -2;
}

var clearMaps = function(parameters)
{
	parameters.PrepareMap = {};			
	parameters.AddMap 	  = {};				
	parameters.RunMap 	  = {};				
	parameters.AddMapMT   = {};				
	parameters.RunMapMT   = {};

	parameters.inputParameters = {};
}

// check if the line is a valid output line
var validOutputLine = function(sCurrentLine)
{
	if(!/\(.*\,.*\)/.test(sCurrentLine) || !validLineHelper(sCurrentLine)){
		return 0;
	}
	return 1;
}

// check if the line is a valid input line
var validInputLine = function(sCurrentLine)
{
	var afterParsed = sCurrentLine.split(/[ ]{1,}/);
	if(!validLineHelper(sCurrentLine) || /\(.*\,.*\)/.test(sCurrentLine)){
		return 0;
	}
	else if(afterParsed[1] != ':'){
		return 0;
	}
	return 1;
}

// Similarities between valid input and output lines
var validLineHelper = function(sCurrentLine){
	if (sCurrentLine.indexOf(':') == -1){
		return false;
	}
	if(sCurrentLine.startsWith('[')       		 ||
		sCurrentLine.startsWith('OUTPUT') 		 ||
		sCurrentLine.startsWith('INPUT')  		 ||
		sCurrentLine.startsWith('>')      		 ||
		sCurrentLine.startsWith('ERROR_MESSAGE') ||
		/^[a-z]/.test(sCurrentLine) ){
		return false;
	}
	return true;
}

var errorOrSkipMessage = function(sCurrentLine)
{
	var k = /^\s*--- \[Failed\].*/;
	var temp = k.test(sCurrentLine);
	if( 
		// (temp) ||
		(sCurrentLine.indexOf("ERROR_MESSAGE") != -1 )		 	||
		(sCurrentLine.indexOf("completed") != -1 ) 				||
		(sCurrentLine.indexOf("Skipped by ALWAYS_SKIP") != -1 ) ||
		( (sCurrentLine.indexOf("Skipped") != -1) && (sCurrentLine.indexOf('[') == -1))
		) {
		return true;
	}
	return false;
}

var isEmpty = function(obj)
{
	for(var prop in obj) {
		if(obj.hasOwnProperty(prop))
			return false;
	}

	return JSON.stringify(obj) === JSON.stringify({});
}

var numberOfProperties = function(obj) {
    var count = 0;
    for(var prop in obj) {
        if(obj.hasOwnProperty(prop))
            ++count;
    }
    return count;
}


var isNumber = function(char)
{
	return /^\d$/.test(char);
}



if (typeof require != 'undefined' && require.main == module) {
	var args = process.argv.slice(2);
	if(args.length != 2){
		console.log("ERROR: Command line arguments invalid");
	}
	else{
		var logFile = args[0];
		var outputLocation = args[1];
		exports.fileparser(logFile, outputLocation, true);
	}
}

