
import sys
import os
import re
import csv
import random
import records
import logging
import optparse
import tempfile
import limits
counter = 0
ct_FlowWriter_process = 0
_VERSION = "1.01"  # 2012-10-26
# version updates
# 1.01  26oct12		updates for 11AC: new substitution functions
# 1.00   3aug11		bump version for windows exe (py2exe-created) package (no code changes in this file)
# 0.95  23may11     fixed write file i/o to not close for every write line, to run faster
# 0.94  20may11     added --duplicates option to disable duplicate test removal
# 0.93  25apr11     fixed a couple of bugs in push flow
# 0.92  18mar11     fixed bug in limit expressions;
# 0.91   8feb11     changes to use python-based substitution strings; corresponding template changes
# 0.9   20jan11     added processing of limits expressions and maps and calculation of limit values;
#                   changes to reading csv files to excel to flowGen works seamlessly; add 
#                   TemplateMgr class for handling template path access; add cmd line option '-t'
#                   for specifying an alternate template directory; update short format header
#                   file with setting and set_parameter lines as comments
# 0.8   30dec10     added processing to remove duplicate tests from test list;
#                   added technology-specific python files
# 0.7   30sep10     added ignoring of whitespace after delimiter in input csv file
# 0.6   30sep10     added support for %%derive...%% macro for EVM_AVG_DB param limit
# 0.5   24sep10     support multiple csv sections in one input file; support the "short"
#                   output format
# 0.4    3sep10     fixed order of technology and RX/TX sequences by making them not arbitrary
# 0.3    2sep10     fixed line processing loop to allow multiple substitutions on a line
# 0.2    2sep10     fixed tx/rx intermingling, added BT templates
# 0.1   27aug10     first version

# TODO List
# * look into using py2exe for packaging into a single executable
# * in short format, ANTENNA is set as setting in root header template and is not being
#   substituted with values from csv; need to fix that
# * we pass flow and test to processFile(); can we create a dict and just pass that?
#       wouldn't that be more convenient for the code that uses this information?
# * support the "W" syntax for WIFI analysis types, e.g. "EMPSRW(10,9,8...)"
# * flow files generated for WIFI_MIMO cannot be read by IQWizard; why?

MULTIRATE_PARAMS     = [ "DATA_RATE", "TEST", "POWER_DBM" ]
MULTIRATE_SEQ_PARAMS = [ "TEST" ]
dbg1 = None
dbg2 = None

# global technology-specific python modules; each technology type can
# have a python module loaded for it; we keep track of them in this global var
#techPyModules_g = {}

# Found the following in Alex's TestAutomation code.
def combinations(*list):
    """ Returns a list of all combination of input list """
    r = [[]]
    for x in list:
        r = [ i + [y] for y in x for i in r ]
        #print ">>>> r = ",r
    return r

def getParamCombinations(rawParamList):
    ''' Returns a list of lists, in which each item in the list is a unique
        combination of parameter values.  The list represents all possible
        combinations of the parameter values.  A sub-item in a list may be
        a list itself, representing a "section" which is iterated over within
        that test.
        rawParamList : a list of lists, in which each primary item in the
                       list represents the values for one parameter that
                       will be iterated.  
        Example: rawParamList = [[2412, 2417, 2422], ['OFDM_6', 'OFDM_12'], 
            ['TX_VERIFY_EVM', 'TX_VERIFY_MASK', 'RX_VERIFY_PER' ], ['15.2', '14.7'],
            ['(0,1,0,0)', '(1,0,0,0)']]   
        Output:  [2412, 'OFDM_6', 'TX_VERIFY_EVM', '15.2', '(0,1,0,0)']
                 [2412, 'OFDM_6', 'TX_VERIFY_EVM', '15.2', '(1,0,0,0)']
                 [2412, 'OFDM_6', 'TX_VERIFY_EVM', '14.7', '(0,1,0,0)']
                 [2412, 'OFDM_6', 'TX_VERIFY_EVM', '14.7', '(1,0,0,0)']
                 [2412, 'OFDM_6', 'TX_VERIFY_MASK', '15.2', '(0,1,0,0)']
                 ....      
    '''
    plist = rawParamList
    # We reverse the list, because combinations() will iterate starting 
    # from the last item, and we want to preserve the user's intended 
    # iteration order as specified from left to right (first to last).
    # However this reverses the order of the parameters, so after running 
    # combinations() we reverse each item in the combos list to get the
    # original parameter order back.
    # I wonder if combinations() could be changed so that this reversing 
    # is not necessary.  I have not spent time looking into that.
    plist.reverse()
    # call the raw combination generator
    combos = combinations(*plist)
    # we don't sort anymore because reversing works better
    #combos.sort()
    for tlist in combos:
        tlist.reverse()
    return combos

class Flow:
    def __init__(self, paramOrder, testList, techName="WIFI"):
        self.testList  = testList
        self.paramOrder  = paramOrder
        self.techName = techName
    
    def getTestList(self):
        return self.testList

    def getTestParams(self, test):
        # Return a dictionary of parameter name keys and parameter values for this test.
        return dict( zip( self.getParamOrder(), test ) )

    # TODO: the 'strip' argument should probably be 'True' by default...
    def getParamOrder(self, strip=True ):
        #Js: Used a lot
        retParams = []
        for param in self.paramOrder:
            if strip:
                retParams.append( param.rstrip('*') )
            else:
                retParams.append( param )
            #print(param)
        #print(retParams)
        return retParams #['DATA_RATE', 'FREQ_MHZ', 'TEST', 'TX_POWER_DBM']

    def getTechName(self):
        return self.techName

    #def getParamNameVars(self, paramName):
    #   return paramName.split("|")

    def getParamIndex(self, paramName):
        ''' Find index of paramName in the paramOrder list.  Any special chars such
            as "*" in the param names in paramOrder are ignored. '''
        ix = 0
        counter = 1
        print(counter)
        for p in self.paramOrder:
            p2 = p.rstrip("*")
            names = p2.split("|")
            if paramName in names:
                return ix
            ix += 1
        return -1

    def getSections(self, test):
        '''
            Flow.getSections()        : return a list of multi-packet sections for a test
            NOT being used
        '''
        # first convert list to a list of lists
        dbg2.debug( "getSections(): enter, test=" + str(test))
        newtest = []
        print("test is ", test)
        for item in test:
            value = item
            print("getSections is ", value)
            if not isinstance(item, list) and not isinstance(item, tuple):
                value = [item]
            newtest.append(value)
        dbg2.debug( "getSections(): newtest=" + str(newtest))
        sections = getParamCombinations( newtest )
        dbg2.debug( "getSections(): sections=" + str(sections))
        return sections
    """
        test = [[2412, 2417, 2422], ['OFDM_6', 'OFDM_12'],
                ['TX_VERIFY_EVM', 'TX_VERIFY_MASK', 'RX_VERIFY_PER'], ['15.2', '14.7'],
                ['(0,1,0,0)', '(1,0,0,0)']]
        sections=[ [2412, 'OFDM_6', 'TX_VERIFY_EVM', '15.2', '(0,1,0,0)']
        [2412, 'OFDM_6', 'TX_VERIFY_EVM', '15.2', '(1,0,0,0)']
        [2412, 'OFDM_6', 'TX_VERIFY_EVM', '14.7', '(0,1,0,0)']
        [2412, 'OFDM_6', 'TX_VERIFY_EVM', '14.7', '(1,0,0,0)']
        [2412, 'OFDM_6', 'TX_VERIFY_MASK', '15.2', '(0,1,0,0)']]
    """
    def getTestName(self, test):
        '''
            Flow.getTestName()        : return the value of the 'TEST' parameter for a given test
                test                  : a list of parameter values representing a test
                returns               : a string which is the value of the 'TEST' parameter
                Being used.
        '''
        #print(test[ self.getParamOrder( True ).index( "TEST" ) ])
        return ( test[ self.getParamOrder( True ).index( "TEST" ) ] )

class FlowCSV(records.RecordDB):
    #flowOrder,
    # It is being used.
    def __init__(self, fname=None, verbose=0):
        print("FlowCSV************************")
        super(FlowCSV,self).__init__(None, verbose)
        csv.register_dialect('flowgen', skipinitialspace=True)
        self.readCsv(fname, 'flowgen')
        print("class FlowCSV\n")
        fh     = open(fname, 'r')
        reader = csv.reader(fh, dialect='flowgen')
        self.flowOrder   = reader.next()
        #print ("flowOrder is ", self.flowOrder)
        #('flowOrder is ', ['TECHNOLOGY', 'DATA_RATE', 'FREQ_MHZ', 'TEST', 'TX_POWER_DBM'])
        fh.close()

    def getFlowOrder(self):
        return self.flowOrder

class FlowReader:
    def __init__(self, randomize=False):
        print("FlowReader***********************")
        self.techList = []
        self.randomize = randomize

    def isLayer2Param(self,paramName):
        return "*" in paramName

    def example(self):
        print "Example .csv file format:"
        print "    TECHNOLOGY,FREQ_MHZ,DATA_RATE,TEST,POWER_DBM,ANTENNA"
        print "    WIFI,2412,OFDM_6,TX_VERIFY_EVM,15.2,\"(0,1,0,0)\""
        print "    WIFI,2417,OFDM_12,TX_VERIFY_MASK,14.7,\"(1,0,0,0)\""
        print "    WIFI,2422,,RX_VERIFY_PER,,"

    def readFlow(self, flowCSVFileName): #read csv to get list of parameters
        print("readFlow is being called\n")
        dbg1.info( "Processing input file: " + flowCSVFileName )
        rec = FlowCSV(flowCSVFileName)  #Key Function to read csv file and put data in rec**
        ###
        for test_parameter,input_value in rec.items():
            print(test_parameter," : ",input_value)
        """
        ('FREQ_MHZ', ' : ', ['2412', '', '', '', '', '', '', ''])
        ('TECHNOLOGY', ' : ', ['WIFI', '', '', '', '', '', '', ''])
        ('DATA_RATE', ' : ', ['OFDM-6', 'OFDM-9', 'OFDM-12', 'OFDM-18', 'OFDM-24', 'OFDM-36', 'OFDM-48', 'OFDM-54'])
        ('TEST', ' : ', ['TX_VERIFY_EVM', '', '', '', '', '', '', ''])
        ('TX_POWER_DBM', ' : ', ['15.0', '', '', '', '', '', '', ''])
        """
        ###
        keyOrder = rec.getFlowOrder()
        valuesList = []
    
        # make the keys all uppercase
        # removed while adding push support (why did we do this?)
        #keyOrder = [x.upper() for x in keyOrder]
    
        dbg1.debug( "keyOrder = %s"%keyOrder )
    
        if "TECHNOLOGY" in keyOrder:
            tech = rec["TECHNOLOGY"][0]
            print("tech is ", tech)
        else:
            print "ERROR: .csv file does not specify the technology.\n       Add 'TECHNOLOGY' key and name to parameters."
            sys.exit(1)
        dbg1.debug( "technology = " + str(tech) )
        keyOrder.remove("TECHNOLOGY")
    
        for key in keyOrder[:]:
            if len(key) == 0:
                #print "ERROR: missing parameter name.  Please check your .csv file.\n"
                #self.example()
                #sys.exit(1)
                # new code below: this is make flowGen work seamlessly with Excel; Excel will add
                # extra commas in the output so that all columns are accounted for; since we allow
                # dividing up the csv file into sections, each with possibly different number of 
                # columns, we need to remove the corresponding extra empty data items from the 
                # data structures
                keyOrder.remove(key)
                if '' in rec:
                    del rec[key]
                continue
            try:
                values = rec[key]
                print("values is : ", values)# ******* CSV content **********************
            except KeyError:
                print "WARNING: no input data found for parameter '%s'"%(key)
                keyOrder.remove(key)
                continue
            dbg2.debug( "record: %s, %s"%(key,values))
            values2 = []
            # get rid of any null values
            """
            ('values is : ', ['OFDM-6', 'OFDM-9', 'OFDM-12', 'OFDM-18', 'OFDM-24', 'OFDM-36', 'OFDM-48', 'OFDM-54'])
            ('v is ', 'OFDM-6')
            ('v is ', 'OFDM-9')
            ('v is ', 'OFDM-12')
            ('v is ', 'OFDM-18')
            ('v is ', 'OFDM-24')
            ('v is ', 'OFDM-36')
            ('v is ', 'OFDM-48')
            ('v is ', 'OFDM-54')
            ('values is : ', ['2412', '', '', '', '', '', '', ''])
            ('v is ', '2412')
            ('values is : ', ['TX_VERIFY_EVM', '', '', '', '', '', '', ''])
            ('v is ', 'TX_VERIFY_EVM')
            ('values is : ', ['15.0', '', '', '', '', '', '', ''])
            ('v is ', '15.0')
            """
            for v in values:
                if v is None:
                    print "ERROR: Missing comma or there is a blank line in .csv input file."
                    print "       Empty fields must be delineated by commas.  No blank lines allowed in .csv file."
                    print "       No output generated.\n"
                    sys.exit(1)

                if len(v.lstrip()) > 0:
                    # convert any numbers to numbers
                    print('v is ', v)
                    try:
                        v = int(v)
                    except:
                        pass
                    values2.append(v)
                    print("values2 is ", values2)
            if self.isLayer2Param(key):
                valuesList.append([values2])
            else:
                valuesList.append(values2)
        dbg1.debug( "valuesList = " + str(valuesList) )
        print("valuesList is ")
        for item in valuesList:
            print(item)
        """
        valuesList is
        ['OFDM-6', 'OFDM-9', 'OFDM-12', 'OFDM-18', 'OFDM-24', 'OFDM-36', 'OFDM-48', 'OFDM-54']
        [2412]
        ['TX_VERIFY_EVM']
        ['15.0']
        ('key order ', ['DATA_RATE', 'FREQ_MHZ', 'TEST', 'TX_POWER_DBM'])
        """
        print("key order ",keyOrder)
        #print ">>>> len(keyOrder) = ",len(keyOrder)
        #print ">>>> len(valuesList) = ",len(valuesList)
        self.extractFlow( keyOrder, valuesList, tech )

    def extractFlow(self, keyOrder, valuesList, technology):
        ''' keyOrder is a list of param names.
            valuesList is a list of param value iterations for each param in keyOrder.
            technology is the name of the technology being used, e.g., "WIFI"'''

        combos = getParamCombinations( valuesList )

        #through here
        print("combos")
        for item in combos:
            print(item)

        #
        if self.randomize: #('self.randomize is ', None)
            # first, do shuffling of any sub-lists (e.g., WIFI_MPS)
            for testParams in combos:
                for params in testParams:
                    if isinstance(params, list) and len(params) > 1: #Not True
                        print("I don't think so")
                        #print ">>>> shuffling sub-list...."
                        random.shuffle(params)
                    print("params")
                    print(params)
            # do random shuffle in place
            #print ">>>> shuffling list...."
            random.shuffle(combos)
        print("self.randomize is ", self.randomize)
        dbg1.debug( "paramOrder = " + str(keyOrder))
        for testParams in combos:
            dbg1.debug( "testParams = " + str(testParams))

        flow = Flow(keyOrder, combos, technology) # Flow contains
        print("flow is ",flow) ## here too
        self.addFlow(technology, flow)

    def addFlow(self, technology, flow):
        # self.techList is [ [techName, [list of flows]], ... ]
        # we need to keep the same technologies together (consecutive), because
        # otherwise it is difficult to use the templates
        #Add flow pass here
        print("AddFlow is here\n")
        print(self.techList)  #[]
        for techData in self.techList: #Not going through
            if techData[0] == technology:
                print("TRUE")
                techData[1].append(flow)
                break
        else:
                # add new technology
            print("False")
            self.techList.append( [technology, [flow]] )
            print(self.techList[0][0])# WIFI, being here*******************************

    def getTechList(self):
        print("getTechList?")
        return self.techList
    #called by FlowWriter(reader.getTechList(), "testFlow.txt").process()

class TemplateMgr:
    def __init__(self, templateDir="templates", outputFormat="iqlite"):
        self.templateDir = templateDir
        self.outputFormat = outputFormat
        self.rootTemplateDir = os.path.join(".", templateDir, outputFormat)
        self.defaultTemplateDir = "templates"
        self.defaultRootTemplateDir = os.path.join(".", self.defaultTemplateDir, outputFormat)
        # make sure a template directory is found
        if not os.path.isdir(self.rootTemplateDir):
            if not os.path.isdir(self.defaultRootTemplateDir):
                print "\nERROR: root template directory '%s' is missing."%self.rootTemplateDir
                print "Program aborted."
                sys.exit(1)
            else:
                print "\nWARNING: root template directory '%s' is missing."%self.rootTemplateDir
                print "      The default template directory '%s' will be used instead."%self.defaultRootTemplateDir
                self.rootTemplateDir = self.defaultRootTemplateDir

        # assign the root template file is found
        self.rootTemplateFile = self.getTemplateFile( "template.txt" )
# push templates do not use a root template!
#        if self.rootTemplateFile == "":
#            print "\nERROR: root template file '%s' is missing."%self.rootTemplateFile
#            print "Program aborted."
#            sys.exit(1)

    def getTemplateFile(self, fileName, technology=None ):
        outFile = ""
        if technology:
            subPath = os.path.join( technology, fileName )
        else:
            subPath = fileName
        tfile = os.path.join( self.rootTemplateDir, subPath )
        if os.path.isfile( tfile ):
            outFile = tfile
        else:
            tfile = os.path.join( self.defaultRootTemplateDir, subPath )
            if os.path.isfile( tfile ):
                outFile = tfile
        return outFile

    def getRootTemplateFile(self):
        ''' Returns the root template file by searching all known template directoruies. Returns "" if not found. '''
#        outRootFile = ""
#        if os.path.isfile( self.rootTemplateFile ):
#            outRootFile = self.rootTemplateFile
#        else:
#            defaultRootFile = os.path.join( self.defaultRootTemplateDir, "template.txt")
#            if os.path.isfile( rootFile ):
#                outRootFile = defaultRootFile
#        return outRootFile
        return self.getTemplateFile( "template.txt" )

    def getTechTemplateFile(self, tech):
#        outTTFile = ""
#        ttfile = os.path.join( self.rootTemplateDir, tech, "template.txt" )
#        if os.path.isfile( ttfile ):
#            outTTFile = ttfile
#        else:
#            ttfile = os.path.join( self.defaultRootTemplateDir, tech, "template.txt" )
#            if os.path.isfile( ttfile ):
#                outTTFile = ttfile
#        return outTTFile
        return self.getTemplateFile( "template.txt", tech )
            
    def getTestTemplateFile(self, flow, fileName):
#        outTTFile = ""
#        ttfile = os.path.join( self.rootTemplateDir, flow.getTechName(), fileName )
#        if os.path.isfile( ttfile ):
#            outTTFile = ttfile
#        else:
#            ttfile = os.path.join( self.defaultRootTemplateDir, flow.getTechName(), fileName )
#            if os.path.isfile( ttfile ):
#                outTTFile = ttfile
#        return outTTFile
        return self.getTemplateFile( fileName, flow.getTechName() )

    def getSectionTemplateFile(self, flow, section, tParam, tValues, tFiles):
        testValue = section[ flow.getParamIndex(tParam) ]

        found = -1
        for i in range(len(tValues)):
            singleVals = testValue.split(",")
            for singleVal in singleVals:
                if tValues[i].count(singleVal) == 0:
                    break
            else:
                found = i
                break
        tFile = tFiles[i]
#        outSTfile = ""
#        STfile = os.path.join( self.rootTemplateDir, flow.getTechName(), tFile )
#        if os.path.isfile( STfile ):
#            outSTfile = STfile
#        else:
#            STfile = os.path.join( self.defaultRootTemplateDir, flow.getTechName(), tFile )
#            if os.path.isfile( STfile ):
#                outSTfile = STfile
#        return outSTfile
        return self.getTemplateFile( tFile, flow.getTechName() )


####################################################################################
#    class:    FlowWriter
class FlowWriter(object):
    # class variables:
    #    techList        :    
    def __init__(self, techList, outFileName="testFlow.txt", outputFormat="iqlite", templateDir="templates", enableDuplicates=False):
        self.techList = techList
        self.outFileName = outFileName
        self.outputFormat = outputFormat
        self.subs = []
        self.templates = TemplateMgr( templateDir, outputFormat )
        self.enableDuplicates = enableDuplicates
        self.testCounter = 0
        self.writecount = 0

    def writeout(self, line ):
        ''' Write text to the output file.   Newlines must be added to the input string by caller.   '''
        #Js,This function is used a lot by writing lines
        if self.writecount == 0:
            self.outFile = open(self.outFileName, 'w')
            #print(self.outFileName), out.txt
        #else:
            #self.outFile = open(self.outFileName, 'a')
        self.outFile.write(line)
        #print(line)
        #self.outFile.close()
        self.writecount += 1
        
    def terminate(self):
        self.outFile.close()
        pass

    def process(self):
        dbg2.debug("FlowWriter.process(): enter")
        global ct_FlowWriter_process
        ct_FlowWriter_process += 1
        print("FlowWriter.process(): enter", ct_FlowWriter_process)
        #self.outFile = open(self.outFileName, 'w')
        fh = open(self.templates.getRootTemplateFile(), "r")
        print(self.templates.getRootTemplateFile())
        text = fh.read()
        fh.close()

        for line in text.splitlines():
            if re.search("%%include\s+([a-zA-Z0-9_\.]+)\s*%%", line):
                obj = re.search("%%include\s+([a-zA-Z0-9_\.]+)\s*%%", line)
                print(obj.group())
                print(obj.group(0))
                print(obj.group(1))
                """
                %%include root_header.txt%%
                %%iterate_tech % %
                %%include root_tail.txt%%
                
               """
                #print(obj.group(1))
                """
                root_header.txt
                root_tail.txt
                """
                self.includeFile(obj.group(1)) #call member function includeFile
    
            elif re.search("%%iterate_tech\s*%%", line):
                print("Enter iterate_tech")
                self.iterateTechList()

                print(self.iterateTechList())
                print("************************")
    
            else:
                self.writeout(line + "\n")
        #self.outFile.close()
        dbg1.info("Done processing input files. Output is in: " + self.outFileName )
        dbg2.debug("FlowWriter.process(): exit")
        #dbg1.info("FlowWriter.process(): exit")

    def process2(self):
        dbg2.debug("FlowWriter.process(): enter")
        print("NEVER entered\n")
        dbg1.info("FlowWriter.process(): enter")

        self.includeFile( "root_header.txt" )
        
        # iterate over test flows to create inputs and results section
        self.iterateTechList()
        
        self.includeFile( "root_tail.txt" )

        dbg1.info("Done processing input files. Output is in: " + self.outFileName )
        dbg2.debug("FlowWriter.process(): exit")

    def processTech(self, techName, techFlowList ):
        '''
            FlowWriter.processTech()            : Processes all the input flows for a given technology.
        '''
        dbg2.debug("FlowWriter.processTech(): enter")
        dbg1.info("FlowWriter.processTech(): enter_Me")
        # load any python code specific for the technology
        #self.loadTechPython( techName )
        
        # get path to technology template file
        tFile = self.templates.getTechTemplateFile( techName )
        print("tFile is ", tFile)#('tFile is ', '.\\templates\\iqlite\\WIFI\\template.txt')

        fh = open( tFile, 'r' )
        text = fh.read()
        fh.close()

        for line in text.splitlines():
            print(">>>> line=",line)
    
            if re.search("%%include\s+([a-zA-Z0-9_\.]+)\s*%%", line):
                obj = re.search("%%include\s+([a-zA-Z0-9_\.]+)\s*%%", line)
                print(obj.group(1))#tech_tail.txt
                self.includeFile(obj.group(1), tech=techName, flow=None, test=None)
    
            elif re.search("%%iterate_flows\s*([a-zA-Z0-9]+)\s*%%", line):
                obj = re.search("%%iterate_flows\s*([a-zA-Z0-9]+)\s*%%", line)
                rootParam = obj.group(1)
                print("OOOOOOOOOOOOOOOOOOOOOOOOO")
                print("rootParam is ",rootParam)
                self.iterateFlows( techName, techFlowList, rootParam=rootParam )
                #self.iterateFlows( techName, techFlowList, rootParam="TEST" )
  
            elif re.search("%%iterate_results\s*%%", line):
                self.iterateResults( techName, techFlowList )
                print("PPPPPPPPPPPPPPPPPPPPPPPPP")
                
            #elif re.search("%%iterate_sequence\s*([a-zA-Z0-9\._]+)\s*%%", line):
            #    obj = re.search("%%iterate_sequence\s*([a-zA-Z0-9\._]+)\s*%%", line)
            #    self.iterateFlows(tech, sequenceFile=obj.group(1))

            elif re.search("%%iterate_sequences", line):
                obj = re.search("%%iterate_sequences\s+(\w+)\s+([a-zA-Z0-9_,:\.]+)\s+([a-zA-Z0-9_,:\.]+)\s*%%", line)
                #self.iterateFlows( techName, techFlowList, rootParam=obj.group(1), tagData=obj.groups()[1:])
                self.iterateFlows( techName, techFlowList, rootParam="TEST",  tagData=("E,M,P,S:sequence_tx.txt", "L,H,S:sequence_rx.txt") )
    
            else:
                self.writeout(line + "\n")

        dbg2.debug("FlowWriter.processTech(): exit")
        dbg1.info("FlowWriter.processTech(): exit")

    def processTech2(self, techName, techFlowList ):
        dbg2.debug("FlowWriter.processTech(): enter")
        dbg1.info("FlowWriter.processTech(): enter processTech2")
        # iterate over tech list to create input section
        self.includeFile( "tech_header.txt", tech=techName )
        
        if techName == "WIFI_MPS":
            self.iterateFlows( techName, techFlowList, rootParam="TEST",  tagData=("E,M,P,S:sequence_tx.txt", "L,H,S:sequence_rx.txt") )
        else:
            self.iterateFlows( techName, techFlowList, rootParam="TEST" )
        self.includeFile( "tech_tail.txt", tech=techName )
        
        dbg2.debug("FlowWriter.processTech(): exit")

#    def loadTechPython( self, technology ):
#        pyFilePrefix = "tech_" + technology.lower()
#        pythonFilePath = self.templates.getTemplateFile( pyFilePrefix + ".py", technology )
#        try:
#            #sys.path.append( os.path.join( self.rootTemplateDir, technology ) )
#            sys.path.append( os.path.dirname( pythonFilePath ) )
#            techPyModules_g[technology] = __import__( pyFilePrefix )
#        except:
#            print "\nERROR: technology python file missing from templates for technology ", technology
#            print "Program aborted."
#            sys.exit(1)

    # python macro function calls (called from in-template expressions)
    def getvalue(self, paramName, argvalue1=None, argvalue2=None ):
        ''' Return param value for current test.  
            Two ways of calling:
                getvalue( paramName, defaultValue )
                getvalue( paramTupleName, index, defaultValue ) '''
        #dbg1.info("getvalue")
        value = ""
        if argvalue2 is None:
            index    = None
            defvalue = argvalue1
        else:
            index    = argvalue1
            defvalue = argvalue2
        if paramName in self.testParams:
            if index is None:
                # normal parameter name
                value = self.testParams[ paramName ]
                #print("value: ", value) #being called
            else:
                # paramName is a tuple (an indexed parameter)
                
                vtuple = eval(self.testParams[paramName])
                vlist = list(vtuple)
                #print("vlist: ",vlist)
                if len(vlist)<= index:
                    # no value for this index yet; this means this parameter is actually using
                    # default values, so we need to add this index and assign the default value;
                    # we use a list to append the defvalue, then convert it to a tuple, then a string;
                    # again, we assume values are being specified in the template file in indexed
                    # order (see comment below)
                    value = defvalue
                    vlist.append( defvalue )
                    tupleStr = str( tuple( vlist ))
                    self.testParams[paramName] = tupleStr
                else:
                    # get the user's value for this indexed parameter
                    value = eval( self.testParams[ paramName ] )[index]
                
            if paramName in self.paramUsageCount:
                self.paramUsageCount[paramName] += 1
        else:
            #print("are we here")
            if index is None:
                if defvalue is not None:
                    value = defvalue
                    # add param using default value to testParams (it may be referenced in another substitution)
                    self.testParams[paramName] = value
            else:
                # add indexed parameter to self.testParams;
                # we assume that when adding indexed params to the testParams that the template enters them in
                # indexed order, that is, 0, 1, 2, 3, etc., otherwise this code would need to be a lot more
                # complicated; I think it is a reasonable assumption...
                if defvalue is not None:
                    value = defvalue
                    tupleStr = str(tuple(defvalue))
                    self.testParams[paramName] = tupleStr
                    
        #print("str(value) is ",str(value))
        return str( value )

    def getvalueAlt(self, paramName1, paramName2, defvalue=None ):
        ''' Check if paramName1 is defined in csv, and return value if so;
            otherwise check if paramName2 is defined, and return value if so;
            else return specifieddefault value.
            Example:
                getvalueAlt( "CH_FREQ_MHZ", "BSS_FREQ_MHZ_PRIMARY", "5520" ) '''
        # print("Enter getvalueAlt: ")# Not been called
        value = ""
        if paramName1 in self.testParams:
            # normal parameter name
            value = self.testParams[ paramName1 ] 
            if paramName1 in self.paramUsageCount:
                self.paramUsageCount[paramName1] += 1
        elif paramName2 in self.testParams:
            # normal parameter name
            value = self.testParams[ paramName2 ] 
            if paramName2 in self.paramUsageCount:
                self.paramUsageCount[paramName2] += 1
        else:
            if defvalue is not None:
                value = defvalue
                    # add param using default value to testParams (it may be referenced in another substitution)
                self.testParams[paramName1] = value
        return str( value )

    def getid(self ):
        self.testCounter += 1
        # print("getid is called: ", self.testCounter)# Not called
        return str( self.testCounter )

    def gettest(self, testName="TEST", defvalue=None ):
        #print("gettest called: ", value) # not used
        value = ""
        if testName in self.testParams:
            value = self.testParams[ "TEST" ]
        else:
            if defvalue is not None:
                value = defvalue
        return str( value )

    def gettech(self):
        print("gettech: ", self.techName)
        return self.techName

    # end macro function calls

    def processFile(self, tFile, flow=None, test=None, sections=None ):
        #This is a main one
        # get template file for test
        dbg2.debug("processFile(): enter")
        dbg2.debug("    tFile=" + tFile + " flow=" + str(flow) + " test=" + str(test))
        print(">>>> procFile(): flow, test = ",flow,test)
        dbg2.debug("    sections=" + str(sections))

        fh = open(tFile, "r")
        text = fh.read()
        fh.close()
        print("tFile: ", tFile)

        linecount = 0
        
        if flow and test:
            #testParams = dict( zip( flow.getParamOrder(), test ) )
            testParams = flow.getTestParams( test )
            print("testParams: ", testParams)
        else:
            testParams = []
        # "globalize" these data so they are accessible from the substitution macro functions 
        # (getValue(), et al) without having to pass them as arguments (keeping it simple)
        self.testParams = testParams
        
        # flag for handling the limitmap case, which can fall over multiple lines
        inLimitMap = False
        
        # now loop over lines in the template file and process each
        for line in text.splitlines():
            #print "\n>>>> line=",line
            linecount += 1

            # check for empty line
            if len(line.split()) == 0 and not inLimitMap:
                self.writeout( line + "\n" )
                continue
                
            if re.search("%%include\s+([a-zA-Z0-9_\.]+)\s*%%", line):
                obj = re.search("%%include\s+([a-zA-Z0-9_\.]+)\s*%%", line)
                self.includeFile(obj.group(1), tech=flow.getTechName(), flow=flow, test=test)
                continue
    
            #elif re.search("%%iterate_section", line):
            #    obj = re.search("%%iterate_section\s+(\w+)\s+([a-zA-Z0-9_,:\.]+)\s+([a-zA-Z0-9_,:\.]+)\s*%%", line)
            #    self.iterateSection(flow, test, obj.group(1), obj.groups()[1:])
            #    continue

            elif re.search("%%iterate_section\s*([a-zA-Z0-9\._]+)\s*%%", line):
                obj = re.search("%%iterate_section\s*([a-zA-Z0-9\._]+)\s*%%", line)
                self.iterateSections(flow, sections, obj.group(1))
    
            elif re.search("%%derive", line):
                # this is a special substitution, based on the values of input parameters
                # currently there can be only one "%%derive" per line
                obj = re.search("%%derive\s+([a-zA-Z0-9\._]+)\s*%%", line)
                if obj:
                    paramName = obj.group(1)
                    paramValue = deriveParamValue(testParams, paramName)
                    newline = line[:obj.start()] + paramValue + line[obj.end():]
                else:
                    obj = re.search("%%derive.*%%", line)
                    if obj:
                        newline = line[:obj.start()] + line[obj.end():]
                    else:
                        # give up trying to figure it out (probably should issue warning message)
                        newline = line
                self.writeout(newline + "\n")

            elif re.search("%%sub", line):
                newline = line
                doneFlag = False
                while not doneFlag:
                    workline = newline[:]
                    obj = re.search("%%sub\s+(.*?)%%", workline)
                    if obj:
                        pystr = obj.group(1)
                        pystr = "self." + pystr.lstrip()
                        paramValue  = eval( pystr )
                        newline = workline[:obj.start()] + paramValue + workline[obj.end():]
                    else:
                        doneFlag = True
                self.writeout(newline + "\n")
            
            elif re.search("%%sub2", line):

                # we found at least one substitution in the line

                paramValue = ""
                paramModifiers = ""
                didASub = False
                newline = line

                # create a dict to hold input params and any default -assigned params
                #print ">>>> testParams = ",testParams
                for i in range(len(flow.getParamOrder())):
                    paramName = flow.getParamOrder()[i]
                    substr = "%%sub2 " + paramName + "(.*?)%%"
                    #if re.search(self.substStrings[i], newline):
                    if re.search(substr, newline):
                        # found a match for one of the input parameters

                         
                        #obj = re.search(self.substStrings[i], newline)
                        obj = re.search(substr, newline)
                        #print ">>>> found subst tag...."
                        #print ">>>> newline = ",newline
                        #print ">>>> substStr = ",self.substStrings[i]
                        #print ">>>> substr = ",substr
                        #print ">>>> obj.group(0) = ",obj.group(0)
                        #print ">>>> obj.start = ",obj.start()
                        #print ">>>> obj.end = ",obj.end()
                        #print ">>>> test[i] = ",test[i]
                        #print ">>>> obj.group(1) = ",obj.group(1)
                        #print ">>>> param = ",flow.getParamOrder()[i]
                        #print ">>>> paramName = ",paramName
                        #print ">>>> testParams = ",testParams
                        paramValue = str(testParams[paramName])
                        paramModifiers = obj.group(1)
                        # apply any modifiers if needed (paramValue may or may not change)
                        paramValue = self.processModifiers(testParams, paramName, paramValue, paramModifiers)
                        # increment the count of this parameter's substitutions
                        if paramName in self.paramUsageCount:
                            self.paramUsageCount[paramName] += 1

                        # make the new line and write it to the output file
                        if obj:
                            #print ">>>> newline before change=",newline
                            newline = newline[:obj.start()] + paramValue + newline[obj.end():]
                            #print ">>>> newline after change=",newline
                            didASub = True
                        else:
                            # should never get here unless the substituion syntax was messed up...
                            print "ERROR: could not process substitution macro, near line ",linecount," of file ",tFile

                # now look for any substitution macros still in the line that were not
                # substituted; we look for the modifiers to get the default value and
                # substitute that
                moreSubsFound = True
                while moreSubsFound:

                    # look for any modifiers; if we don't match any modifiers then warn the 
                    # user of an empty param value
                    paramName = "???"
                    paramValue = ""
                    substr = "%%sub2 ([a-zA-Z0-9_]+)\s(.*?)%%"
                    if re.search(substr, newline):
                        # found a sub macro with modifiers
                        obj = re.search(substr, newline)
                        paramName = obj.group(1)
                        paramModifiers = obj.group(2)
                    else:
                        # try to make a basic match so we can eliminate the substitution macro
                        substr = "%%sub2 ([a-zA-Z0-9_]+)\s*%%"
                        if re.search(substr, newline):
                            # found a sub macro with no modifiers, well, get the paramName...
                            obj = re.search(substr, newline)
                            paramName = obj.group(1)
                        else:
                            # no more sub macros, stop looking
                            moreSubsFound = False
                            break
                    if paramModifiers == "":
                        print "WARNING: No parameter value match found for '%s'"%(paramName)
                        print "         You will need to add this parameter to the input list, or edit"
                        print "         the output test file manually."

                    paramValue = self.processModifiers(testParams, paramName, paramValue, paramModifiers)
                    # make the new line and write it to the output file
                    if obj:
                        newline = newline[:obj.start()] + paramValue + newline[obj.end():]
                        didASub = True
                    else:
                        # should never get here unless the substituion syntax was messed up...
                        print "ERROR: could not process substitution macro, near line ",linecount," of file ",tFile

                self.writeout(newline + "\n")

# handle limit expressions and limit maps
#
#    algorithm:
#    ...
#    else:
#        if not inLimitMap:
#            newline = ""
#        while line is not "":
#            if not inLimitMap:
#                if "lim" found:
#                    break into portions
#                    compute limit
#                    newline = newline + ( line before macro ) + limit
#                    line = (line after macro)
#                else if "lmap" found:
#                    inLimitMap = true
#                    create LimitMap object
#                    newline = newline + ( line before macro )
#                    line = (line from start of macro to end of line)
#                else:
#                    newline = newline + line
#                    line = ""
#                    write out newline
#            else: ( if inLimitMap )
#                get portions of matching string
#                append macro data on line to LimitMap object
#                line = (line after macro data)
#                if end of substition was on line:
#                    inLimitMap = false
#                    build map table and compute limit
#                    newline = newline + limit 

            else:
                if not inLimitMap:
                    newline = ""
                while len(line) > 0:
                    if not inLimitMap:
                        if re.search("%%lim ", line):
                            obj = re.search( "%%lim\s+([^%]*)\s*%%\s*", line )
                            if obj:
                                #limitExpr = limits.LimitExpr_t( flow, test )
                                #limit = limitExpr.getLimit( obj.group(1) )
                                #limit = limits.evalExpr( flow, test, obj.group(1) )
                                limit = limits.evalExpr( self.testParams, obj.group(1) )
                                newline = newline + line[ :obj.start() ] + limit
                                line = line[ obj.end(): ]
                            else:
                                print ("Error: invalid limit expression, near line ",linecount," of file ",tFile)
                                sys.exit(1)
                        elif re.search("%%lmap", line):
                            obj = re.search( "%%lmap\s*([^%]*)\s*(%%)*\s*", line)
                            if obj:
                                inLimitMap = True
                                #limitMap = limits.LimitMap_t( flow, test )
                                limitMap = limits.LimitMap_t( self.testParams )
                                newline = newline + line[:obj.start()]
                                line = line[obj.start():]           # truncate the line;
                            else:
                                print "Error: expected limit map parameter list not found, near line ",linecount," of file ",tFile
                                sys.exit(1)
                        else:
                            # lines with no directives come here, and also remainder of lines with no more directives left 
                            newline = newline + line
                            line = ""
                            self.writeout( newline + "\n" )
                    else:
                        obj = re.search( "(%%lmap)*\s*([^%]*)\s*(%%)*\s*", line)
                        if obj:
                            # the first group, if present, is the "%%lmap"
                            # the second group is the string of data inside the macro
                            # the third group, if present, is the macro termination string "%%"
                            limitMap.append( obj.group(2) )
                            line = line[obj.end():]
                            if obj.group(3):
                                # end of limit map found
                                inLimitMap = False
                                # TODO: compute limit value
                                limitValue = limitMap.getLimit()
                                newline = newline  + limitValue
                        else:
                            print "Error: expected limit map parameter expression not found, near line ",linecount," of file ",tFile
                            sys.exit(1)
                        
        dbg2.debug("processFile(): exit")
    
    def processModifiers(self, testParams, paramName, paramValue, paramModifiers ):

        newValue = paramValue

        # look for any modifier tags; modifiers follow the last "_" in substitution tag;
        # e.g., "ANTENNA_1" or "TX_VERIFY_PER_DEV=1.5"
        # if no matching modifier found, just substitute the parameter value 
        modifiersList = self.parseModifier( paramModifiers )
        if len(modifiersList) > 0:

            # look for the DEFAULT modifier and process it first, since other 
            # modifiers may depend on a param value
            for modifier in modifiersList:
                if modifier[0][0:3] == "DEF":
                    # substitute the default value if there was no parameter specified
                    #if newValue == "":
                    #    newValue = modifier[1]
                    #    print ">>>> adding def value, param name, value = ",paramName,paramValue
                    #    testParams[paramName] = paramValue
                    if paramName not in testParams:
                        newValue = modifier[1]
                        testParams[paramName] = newValue

            # process remaining modifiers
            for modifier in modifiersList:

                # check for tuple index specifier: e.g., "IX=0"
                # this is for processing the ANTENNA special parameter
                if modifier[0] == "INDEX":
                    # get integer index
                    ix = int(modifier[1])
                    # check for a tuple value; expect an integer modifier to indicate index to get value
                    try:
                        #if isinstance( eval( test[i] ), tuple):
                        if isinstance( eval( testParams[paramName] ), tuple):
                            #print ">>>> found a tuple...."
                            #print ">>>> test[i] = ",test[i]
                            #print ">>>> tuple ix = ",ix
                            #tupleData = eval(test[i])
                            tupleData = eval(testParams[paramName])
                            #print ">>>> tupleData = ", tupleData
                            #print ">>>> ix, tupleData[ix] = ", ix, tupleData[ix]
                            # ok, found the indexed value, so use it
                            newValue = str(tupleData[ix])
                    except (NameError,TypeError,SyntaxError):
                        # not a tuple will cause exception: just continue
                        pass
                    except KeyError:
                        #print "ERROR: No input value specified for parameter '%s'"%(paramName)
                        # user did not specify input, no default specified, so hard code this puppy
                        # this is equivalent to 1,0,0,0
                        if ix == 0: newValue = '1'
                        else:       newValue = '0'

                # check for "DEV=<num>" modifier: used for limits deviation
                if modifier[0] == "LIMITDEV":
                    deviation = float(modifier[1])
                    lower_limit = float(testParams[paramName]) - deviation
                    upper_limit = float(testParams[paramName]) + deviation
                    newValue = str(lower_limit) + "," + str(upper_limit)

        return newValue

    def getTestTemplateName(self, flow, test ):
        testNamePrefix = flow.getTestName( test )
        return testNamePrefix + ".txt"
    
    def iterateTechList(self):
        # self.techList is a list of 'tech flows', where each 'tech flow' contains
        # the list of flows for that technology
        for techData in self.techList:
            techName = techData[0]
            techFlowList = techData[1]
            # save the technology name in the class scope so we can access it from the macro 
            # functions easier (gettech(), specifically)
            self.techName = techName
            self.processTech( techName, techFlowList )

    def iterateFlows(self, techName, techFlowList, rootParam=None, tagData=None ):
        dbg2.debug("iterateFlows(): enter, tech= " + str(techName) )
        # a 'techFlow' is a list of flows of the same technology
        # self.flows is a list of techFlows
        # find the list of flows for this technology
        # for techData in self.techList:
        #    if techData[0] == tech:
        #        flows = techData[1]
        # for flow in flows:
        for flow in techFlowList:
            
            # "globalize" these data so they are accessible from the substitution macro functions 
            # (getValue(), et al) without having to pass them as arguments (keeping it simple)
            self.currentFlow = flow

            # we count the number of times that each parameter substitution is done,
            # so we can write warnings if a user-specified parameter was not used (due to
            # no substitution perhaps)
            self.paramUsageCount = {}
            for param in flow.getParamOrder():
                self.paramUsageCount[param] = 0
            try: del self.paramUsageCount['TEST']
            except KeyError: pass

            if not tagData and not self.enableDuplicates:
                # analyze the flow and find and remove any duplicate tests (non-MPS case)
                FlowAnalyzer( flow, self ).removeDuplicateTests()
            dummy = 1
                    
            # we use the sequenceFile if specified, otherwsise look at the specified 
            # param, to get the template file
            #if sequenceFile:
            #    for test in flow.getTestList():
            #        tFilePath = self.getTestTemplateFile(flow, sequenceFile)
            #        self.processFile(tFilePath, flow, test)
            #else:
            #    for test in flow.getTestList():
            #        filePrefix = test[ flow.getParamOrder().index(rootParam) ]
            #        tFile = self.getTestTemplateFile(flow, filePrefix + ".txt" )
            #        self.processFile(tFile, flow, test)
            for test in flow.getTestList():
                # "globalize" these data so they are accessible from the substitution macro functions 
                # (getValue(), et al) without having to pass them as arguments (keeping it simple)
                self.currentTest = test
                
                if tagData:
                    self.iterateSequence(flow, test, rootParam, tagData)
                    #tFile = self.getTestTemplateFile(flow, sequenceFile)
                else:
            
                    testTemplateName = self.getTestTemplateName( flow, test )
                    tFile = self.templates.getTestTemplateFile(flow, testTemplateName )
                    self.processFile( tFile, flow=flow, test=test )

            #print "paramUsageCount: ",self.paramUsageCount
            for (key, value) in self.paramUsageCount.iteritems():
                if value == 0:
                    print "WARNING: There were no value substitutions for parameter '%s'."%(key)
                    print "         Possibly the templates do not have a substitution macro defined for it."
        dbg2.debug("iterateFlows(): exit")

    def iterateSequence(self, flow, test, tagParam, tagData):
        '''
            flow:     the Flow object representing this technology's group of tests. 
            test:     a list of the param values to be used when processing this section.
            tagParam: the first argument in the '%%iterate_section' directive,
                      it is the name of a parameter, typically 'TEST'
            tagData:  the remaining arguments, each of which is in the format
                      'value1, value2,...:fileName' which means that if the tagParam's
                      values are all in these set of values, then use the specified file
                      after the colon as the template, else move on and check the new
                      next argument for a match.  The purpose is to identify the proper
                      template file to use for this section based on the value of the 
                      tagParam parameter.
                      Example: 
                          '%%iterate_section TEST E,M,P,S:TX_TEST_ADD.txt L,H,S:RX_TEST_ADD.txt'
        '''
        dbg2.debug("iterateSequence(): enter")
        dbg2.debug("iterateSequence(): tagParam = " + str(tagParam))
        dbg2.debug("iterateSequence(): tagData = " + str(tagData))
        #print ">>>> it_sec(): test = ",test
        #print ">>>> it_sec(): tagParam = ",tagParam
        #print ">>>> it_sec(): tagData = ",tagData
        tValues = []
        tFiles  = []
        for tag in tagData:
            items = tag.split(":")
            values = items[0].split(",")
            tValues.append(values)
            tFiles.append(items[1])
        dbg2.debug( "tValues = " + str(tValues))
        dbg2.debug( "tFiles = " + str(tFiles))
        sections = flow.getSections(test)
        dbg2.debug( "iterateSequence():     sections = " + str(sections))

        if not self.enableDuplicates:
            FlowAnalyzer( flow, self, sections ).removeDuplicateTests()
        
        typeSections = []
        #print ">>>> sections = ",sections
        for section in sections:
            testValue = section[ flow.getParamIndex(tagParam) ]
            for i in range(len(tValues)):
                singleVals = testValue.split(",")
                for singleVal in singleVals:
                    if tValues[i].count(singleVal) == 0:
                        break
                else:
                    for typeSecs in typeSections:
                        if typeSecs[0] == tFiles[i]:
                            typeSecs[1].append(section)
                            break
                    else:
                        typeSections.append( [ tFiles[i], [section] ] )

                    break
        #print ">>>> typeSections = ",typeSections

        #for (secTFile, sections) in typeSections.iteritems():
        for typeSecs in typeSections:
            secTFile = typeSecs[0]
            sections = typeSecs[1]
            secTFile = self.templates.getTestTemplateFile(flow, secTFile)
            self.processFile(secTFile, flow=flow, test=test, sections=sections)
       
        # original 
        #for section in sections:
        #    tFile = self.getSectionTemplateFile(flow, section, tagParam, tValues, tFiles) 
        #    self.processFile(tFile, flow, section)

        # new

        dbg2.debug("iterateSequence(): exit")

    def iterateSections(self, flow, sections, sectionFile):
        dbg2.debug("iterateSections(): enter, flow=" + str(flow) +" sectionFile=" + sectionFile)
        dbg2.debug("iterateSections():        sections=" + str(sections))
        sectionFilePath = self.templates.getTestTemplateFile(flow, sectionFile)
        for section in sections:
            self.processFile(sectionFilePath, flow=flow, test=section)
        dbg2.debug("iterateSections(): exit")

    def iterateResults(self, techName, techFlowList ):
        ''' FlowWriter.iterateReulsts(): expected implemented in derived class. '''
        pass

    def includeFile(self, tFile, tech=None, flow=None, test=None):
        #print ">>>> includeFile(), tFile = ",tFile," tech = ",tech," flow = ",flow
#        if tech:
#            tFile = os.path.join(tech, tFile)
#        tFile = os.path.join(self.rootTemplateDir, tFile)
        tFile = self.templates.getTemplateFile( tFile, tech )
        dbg2.debug( "including file: " + tFile )
        self.processFile( tFile, flow=flow, test=test )

    def parseModifier(self, paramStr):
        modsList = []
        #ix = paramStr.rfind("_")
        #if ix >= 0:
        #    modifier = paramStr[ix+1:]
        #    modList = modifier.split("=")

        mList = paramStr.lstrip().rstrip().split()
        for mod in mList:
            modsList.append( mod.split("=") )
        return modsList

    def setup_sub(self, paramName, findstr, oldstr, newstr):
        self.subs.append(dict( param=paramName, findstr=findstr, oldstr=oldstr, newstr=newstr ))
        #print "subs = ",self.subs
        
    def getFlowTemplateFiles( self, testName ):
        ''' Return a list of template files used to generate tests for a specific technology and output format. 
            This is used to search for parameter usage when processing the test list to removing duplicate
            test entries. '''
        tFileList = []
        tech = self.currentFlow.getTechName()
        #tFileList.append( "templates/iqlite/WIFI/" + testName + ".txt" )
        tFileList.append( self.templates.getTemplateFile(  testName + ".txt", tech ) )
        return tFileList

class IqliteWriter( FlowWriter ):
    
    def getFlowTemplateFiles( self, testName ):
        ''' Return a list of template files used to generate tests for a specific technology and output format. 
            This is used to search for parameter usage when processing the test list to removing duplicate
            test entries. '''
        tFileList = []
        tech = self.currentFlow.getTechName()
        if tech == "WIFI_MPS":
            tFileList.append( self.templates.getTemplateFile( "TEST_PREPARE.txt", tech ) )
            if "L" in testName or "R" in testName:
                tFileList.append( self.templates.getTemplateFile( "RX_TEST_ADD.txt", tech ) )
            else:
                tFileList.append( self.templates.getTemplateFile( "TX_TEST_ADD.txt", tech ) )
        else:
            tFileList = super(IqliteWriter, self).getFlowTemplateFiles( testName )
        return tFileList

    def get11AC_CH_BW(self, bss_bw_paramName, argvalue1=None ):
        ''' Return param value for current test.  
                getvalue( paramName, defaultValue ) '''
        value = ""
        defvalue = argvalue1
        ch_bw_paramName = "CH_BANDWIDTH"
        if bss_bw_paramName in self.testParams:
            bss_bw_value = self.testParams[ bss_bw_paramName ]
            if bss_bw_value == "BW-20":
                value = "CBW-20"
            elif bss_bw_value == "BW-40":
                value = "CBW-40"
            elif bss_bw_value == "BW-80":
                value = "CBW-80"
            else:
                value = "ERROR_COULD_NOT_GET_CH_BANDWIDTH_VALUE"
        else:
            if defvalue is not None:
                value = defvalue
                # add param using default value to testParams (it may be referenced in another substitution)
                self.testParams[ch_bw_paramName] = value
            else:
                value = "ERROR_UNKNOWN_CH_BANDWIDTH_DEF_VALUE"
                    
        return str( value )

class ShortWriter( FlowWriter ):
    def getFlowTemplateFiles( self, testName ):
        ''' Return a list of template files used to generate tests for a specific technology and output format. 
            This is used to search for parameter usage when processing the test list to removing duplicate
            test entries. '''
        tFileList = []
        tech = self.currentFlow.getTechName()
        if tech == "WIFI_MPS":
            if "L" in testName or "R" in testName:
                tFileList.append( self.templates.getTemplateFile( "rx_add.txt", tech ) )
            else:
                tFileList.append( self.templates.getTemplateFile( "tx_add.txt", tech ) )
        else:
            tFileList = super(ShortWriter, self).getFlowTemplateFiles( testName )
        return tFileList

class PushWriter( FlowWriter ):
    
    def process2(self):
        ''' Override of FlowWriter.process() for Push flow. '''
        dbg2.debug("PushWriter.process(): enter")
        dbg1.info("PushWriter.process(): Never Entered..*****************")
        #self.outFile = open( self.outFileName, 'w' )

        self.includeFile( "root_header.txt" )
        
        # iterate over test flows to create inputs and results section
        self.iterateTechList()
        
        self.includeFile( "tester_settings.txt" )
        self.includeFile( "root_tail.txt" )

        #self.outFile.close()
        dbg1.info("Done processing input files. Output is in: " + self.outFileName )
        dbg2.debug("PushWriter.process(): exit")
        
        
    def processTech2(self, techName, techFlowList ):
        ''' Override of FlowWriter.processTech() for Push flow. 
            Processes all the input flows for a given technology. '''
        dbg2.debug("PushWriter.processTech(): enter")
        
        # load any python code specific for the technology
        #self.loadTechPython( techName )

        # iterate over tech list to create input section
        self.includeFile( "testflow_hdr.txt" )
        self.iterateFlows( techName, techFlowList )
        self.includeFile( "testflow_tail.txt" )

        # iterate over tech list again to do results section
        self.includeFile( "results_limits_hdr.txt" )
        self.iterateResults( techName, techFlowList )
        self.includeFile( "results_limits_tail.txt" )

        dbg2.debug("PushWriter.processTech(): exit")

    def iterateResults(self, techName, techFlowList ):
        dbg2.debug("iterateResults(): enter, tech= " + str( techName ) )
        
        self.testCounter = 0
        for flow in techFlowList:
            # "globalize" these data so they are accessible from the substitution macro functions 
            # (getValue(), et al) without having to pass them as arguments (keeping it simple)
            self.currentFlow = flow
            for test in flow.getTestList():
                
                # "globalize" these data so they are accessible from the substitution macro functions 
                # (getValue(), et al) without having to pass them as arguments (keeping it simple)
                self.currentTest = test

                self.includeFile( "testresult_hdr.txt", techName )
                #testParams = dict( zip( flow.getParamOrder(), test ) )
                testParams = flow.getTestParams( test )

                rateType = self.getRateType( testParams["rate"] )
                testTypes = self.getTestTypes( testParams["TEST"] )
                resultTemplateFileList = []
                for testName in testTypes:
                    rootFile = None
                    if testName == "evm":
                        rootFile = "evm_" + rateType + "_results.txt"
                    elif testName == "mask":
                        rootFile = "mask_" + rateType + "_results.txt"
                    elif testName == "power":
                        rootFile = "power_results.txt"
                    elif testName == "rx":
                        rootFile = "rx_results.txt"
                    if rootFile:
                        resultTemplateFileList.append( self.templates.getTestTemplateFile( flow, rootFile ) )
                for tFile in resultTemplateFileList:
                    self.processFile( tFile, flow=flow, test=test )
                self.includeFile( "testresult_tail.txt", techName )

        dbg2.debug("iterateResults(): exit")

    def getRateType(self, rate ):
        rateType = "unknown"
        if rate.find( "DSSS" ) >= 0:
            rateType = "802.11b"
        elif rate.find( "CCK" ) >= 0:
            rateType = "802.11b"
        elif rate.find( "OFDM") >= 0:
            rateType = "802.11ag"
        elif rate.find( "MCS") >= 0:
            rateType = "802.11n"
        return rateType

    def getTestTemplateName(self, flow, test ):
        testName = flow.getTestName( test )
        if "rx" in testName.lower():
            return "rx_test.txt" 
        else:
            return "tx_test.txt"

    def getTestTypes(self, testName ):
        testTypes = []
        testName = testName.lower()
        testTypes = testName.split("_")
        if 'tx' in testTypes:
            testTypes.remove('tx')
        return testTypes

    def gettest(self, testName=None, defvalue=None ):
        value = "Disable"
        if testName in self.getTestTypes( self.testParams["TEST"] ):
            value = "Enable"
        else:
            if defvalue is not None:
                value = defvalue
        return str( value )

#    def getvalue(self, paramName, defvalue=None, ):
#        value = ""
#        if paramName == "startPower" or paramName == "stopPower" or paramName == "step":
#            if "power_range" in self.testParams.keys():
#                powerValues = eval( self.testParams["power_range"])
#                if paramName == "startPower":
#                    value = powerValues[0]
#                elif paramName == "stopPower":
#                    value = powerValues[1]
#                elif paramName == "step":
#                    value = powerValues[2]
#            else:
#                if defvalue is not None:
#                    value = defvalue
#        else:
#            value = super(PushWriter, self).getvalue( paramName, defvalue=defvalue )
#        return str( value )

    def getFlowTemplateFiles( self, testName ):
        ''' Return a list of template files used to generate tests for a specific technology and output format. 
            This is used to search for parameter usage when processing the test list to removing duplicate
            test entries. '''
        tFileList = []
        tech = self.currentFlow.getTechName()
        if "rx" in testName.lower():
            tFileList.append( self.templates.getTemplateFile( "rx_test.txt", tech ) )
        else:
            tFileList.append( self.templates.getTemplateFile( "tx_test.txt", tech ) )
        return tFileList

class FlowAnalyzer:
    '''
        class: FlowAnalyzer            : Perform modifications on an existing flow, e.g. remove
                                         duplicate tests.
    '''
    def __init__(self, flow, writer, testList=None ):
        self.flow = flow
        if not testList:
            self.testList = flow.getTestList()
        else:
            self.testList = testList
        self.writer = writer
        
    def __buildValidParamsList(self):
        # build a dict listing valid params for each test
        validParams = {}
        paramNames = self.flow.getParamOrder()[:]
        paramNames.remove( "TEST" )
        for test in self.testList:
            testName = self.flow.getTestName( test )
            if testName not in validParams:
                validParams[testName] = []
                checkParamNames = paramNames[:]
                #testTemplateFiles = techPyModules_g[self.flow.getTechName()].getTestTemplateFiles( testName )
                testTemplateFiles = self.writer.getFlowTemplateFiles( testName )
                for tFile in testTemplateFiles:
                    for line in open( tFile ):
                        for paramName in checkParamNames[:]:
                            if paramName in line:
                                validParams[testName].append( paramName )
                                checkParamNames.remove(paramName)
                        if len(checkParamNames) == 0:
                            break
                    if len(checkParamNames) == 0:
                        break
        return validParams

    def __buildModFlowList(self):
        
        validParams = self.__buildValidParamsList()
       
        # build modified flow list with only valid params and the 'TEST' name
        modFlow = []
        paramNames = self.flow.getParamOrder()[:]
        #for test in self.flow.getTestList():
        for test in self.testList:
            testName = self.flow.getTestName( test )
            modTest = []
            ix = 0
            for param in paramNames:
                
                if param == "TEST" or param in validParams[testName]:
                    modTest.append( test[ix] )
                ix += 1
            modFlow.append(modTest)
        return modFlow
 
    def __getDuplicateList(self):
        
        modifiedFlow = self.__buildModFlowList()

        # hmmm, there might be a better way to do this...
        
        # create and init duplicates array for flow
        #flowDupFlags = []
        #for test in self.flow.getTestList():
        #   flowDupFlags.append( False )
        #flowDupFlags = [False]*len(self.flow.getTestList())
        flowDupFlags = [False]*len(self.testList)

        # analyze modFlow for duplicate entries and set flowDupFlags
        for ix in range( len( modifiedFlow )):
            if not flowDupFlags[ix]:
                for ix2 in range( ix+1, len( modifiedFlow) ):
                    if len(modifiedFlow[ix]) != len(modifiedFlow[ix2]) :
                        break
                    for p_ix in range( len(modifiedFlow[ix]) ):
                        if modifiedFlow[ix][p_ix] != modifiedFlow[ix2][p_ix] :
                            break
                    else:
                        flowDupFlags[ix2] = True
        return flowDupFlags
    
    def __removeTests(self, removeFlags ):
        # now use flowDupFlags to remove duplicate items from 'flow'
        #flowList = self.flow.getTestList()
        flowList = self.testList
        for ix in range( len( removeFlags )-1, -1, -1 ):
            if removeFlags[ix]:
                dbg1.info("Removing duplicate test from list: " + str(flowList[ix]) )
                flowList.pop( ix )
        return
    
    def removeDuplicateTests( self ):
        flowDupFlags = self.__getDuplicateList()
        self.__removeTests( flowDupFlags )
        return

def deriveParamValue(testParams, paramName, defValue=""):
    import limits
    if paramName == "EVM_AVG_DB":
        try:
            depParam = "DATA_RATE"
            dataRate = testParams[depParam]
        except KeyError:
            print "WARNING: cannot derive limit for parameter '%s'."%(paramName)
            print "    Dependent parameter '%s' is not an input parameter or cannot be determined."%(depParam)
            # let it return the default value
            return limits.get_EVM_AVG_DB_limit("")
        return limits.get_EVM_AVG_DB_limit(dataRate)
    else:
        return defValue
    return defValue

def testing():
    reader = FlowReader()

    paramOrder1 = [ "FREQ_MHZ", "DATA_RATE", "TEST", "POWER_DBM", "ANTENNA" ]
    params1 = ( (2412,2417,2422), ("OFDM_6","OFDM_12"), ("TX_VERIFY_EVM","TX_VERIFY_MASK","RX_VERIFY_PER"), (15.2,14.7), ("(0,1,0,0)", "(1,0,0,0)" ) )
    #reader.extractFlow( paramOrder1, params1, "WIFI" )
    #reader.readFlow("flow.csv")
    #reader.readFlow("flow2.csv")

    paramOrder2 = [ "FREQ_MHZ", "DATA_RATE", "TEST", "POWER_DBM", "ANTENNA" ]
    params2 = ( (2412,2417,2422), (("OFDM_6","OFDM_12"),), (("E,M,P","E,M,P,S","L,H,S"),), ((15.2,14.7),), ("(0,1,0,0)", "(1,0,0,0)" ) )
    #reader.extractFlow( paramOrder2, params2, "WIFI_MPS" )
    reader.readFlow("multirate_flow.csv")

    FlowWriter(reader.getTechList(), "testFlow.txt").process()

def isDividerLine( line ):
    ''' Checks if the line is empty, or all commas. '''
    isDivider = False
    tokens = line.split()
    if len(tokens) == 0:
        isDivider = True
    else:
        if len(tokens) == 1:
            token = tokens[0]
            if token.count(",") == len(token):
                # line is all commas
                isDivider = True
    return isDivider

def preprocessFile(inputFile):
    csvFilesList = []
    tmpFilesList = []
    tempFName    = ""
    fp = open(inputFile, 'r')

    # first pass, find how many distinct csv sections there are
    # we make two passes, the first only to count the sections, so we can quickly
    # determine the simple 1-section case, and avoid having to create temp files
    numSections = 0
    newSectionFound = False
    lines = fp.readlines()
    for line in lines:
        #tokens = line.split()
        #if len(tokens) == 0:
        if isDividerLine( line ):
            newSectionFound = False
        else:
            if not newSectionFound:
                newSectionFound = True
                numSections += 1

    if numSections <= 1:
        # no sections, so no need to split into files, just use this one
        fp.close()
        return ([inputFile], [])

    # multiple sections were found, so we need to split into temporary files

    # second pass
    numSections = 0
    newSectionFound = False
    tempFp = None
    for line in lines:
        #tokens = line.split()
        #if len(tokens) == 0:
        if isDividerLine( line ):
            if newSectionFound and tempFp:
                csvFilesList.append(tempFName)
                tmpFilesList.append(tempFName)
                tempFp.close()
                tempFp = None
            newSectionFound = False
        else:
            if not newSectionFound:
                newSectionFound = True
                numSections += 1
                # for 2.5:
                (tempFd, tempFName) = tempfile.mkstemp(text=True)
                tempFp = os.fdopen(tempFd, "w")
                # for 2.6 and later, use the following:
                #tempFp = tempfile.NamedTemporaryFile(delete=False)
                # tempFName = tempFp.name
            tempFp.write(line)
    if tempFp:
        csvFilesList.append(tempFName)
        tmpFilesList.append(tempFName)
        tempFp.close()
        tempFp = None
    return (csvFilesList, tmpFilesList)
              

def getInputFiles(cmdArgs):
    csvFilesList = []
    tmpFilesList = []
    for inputFile in cmdArgs:
        (csvFiles, tmpFiles) = preprocessFile(inputFile)
        for csvFile in csvFiles:
            csvFilesList.append(csvFile)
        for tmpFile in tmpFiles:
            tmpFilesList.append(tmpFile)
    return (csvFilesList, tmpFilesList)

def setupDebug( debug1=False, debug2=False):
    global dbg1, dbg2
    dbg1 = logging.getLogger("L1")
    h = logging.StreamHandler()
    #h.setFormatter( logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s" ))
    h.setFormatter( logging.Formatter("%(levelname)s: %(message)s" ))
    dbg1.addHandler( h )
    if debug1 or debug2:
        dbg1.setLevel(logging.DEBUG)
    else:
        dbg1.setLevel(logging.INFO)
    dbg1.debug("Debug Level 1 Messages On!")

    dbg2 = logging.getLogger("L2")
    h = logging.StreamHandler()
    #h.setFormatter( logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s" ))
    h.setFormatter( logging.Formatter("%(levelname)s: %(message)s" ))
    dbg2.addHandler( h )
    if debug2:
        dbg2.setLevel(logging.DEBUG)
    dbg2.debug("Debug Level 2 Messages On!")

def getWriter( outputFormat ):
    s = outputFormat.capitalize()
    s = "%sWriter"%(s)
    return globals()[s]
    
def setupOptions():
    usage = "usage: %prog csvfile [csvfile]* [options]"
    parser = optparse.OptionParser(usage)
    parser.add_option("-d", "--duplicates",  action="store_true", dest="enableDuplicates", default=False)
    parser.add_option("-1", "--debug1", action="store_true", dest="debug1")
    parser.add_option("-2", "--debug2", action="store_true", dest="debug2")
    parser.add_option("-r", "--randomize", action="store_true", dest="randomize")
    parser.add_option("-f", "--format", dest="outputFormat",  default="iqlite",
                      help="output format", metavar="FORMAT")
    parser.add_option("-o", "--output", dest="outFileName",  default="test_flow.txt",
                      help="output file", metavar="FILE")
    parser.add_option("-t", "--templatedir", dest="templateDirName",  default="templates",
                      help="template directory", metavar="DIR")
    (options, args) = parser.parse_args()
    #if len(args) != 1:
    #    parser.error("ERROR: no input files specified.")
    #    sys.exit(1)
    return (options, args)

def run( params, values, technology, output_file):
    global dbg1, dbg2
    (options, args) = setupOptions()
    setupDebug( options.debug1, options.debug2 )
    reader = FlowReader(randomize=options.randomize)
    reader.extractFlow( params, values, technology )
    writerInst = FlowWriter(reader.getTechList(), outFileName=output_file)
    writerInst.process()
    writerInst.terminate()

def main():
    (options, args) = setupOptions()
    setupDebug( options.debug1, options.debug2 )
    if len( args ) == 0:
        print ("ERROR: no input files specified. ")
        sys.exit(1)
    reader = FlowReader(randomize=options.randomize)
    (csvFilesList, tempFilesList) = getInputFiles(args)
    #print "csvFilesList = ",csvFilesList
    #print "tempFilesList = ",tempFilesList
    for csvFile in csvFilesList:
        reader.readFlow(csvFile)

#    FlowWriter( reader.getTechList(), 
#                outFileName=options.outFileName, 
#                outputFormat=options.outputFormat,
#                templateDir=options.templateDirName ).process()
    writerClass = getWriter( options.outputFormat )
#    writerClass( reader.getTechList(), 
#                 outFileName=options.outFileName, 
#                 outputFormat=options.outputFormat, 
#                 templateDir=options.templateDirName,
#                 enableDuplicates=options.enableDuplicates).process()
    writerInst = writerClass( reader.getTechList(), 
                 outFileName=options.outFileName, 
                 outputFormat=options.outputFormat, 
                 templateDir=options.templateDirName,
                 enableDuplicates=options.enableDuplicates)
    writerInst.process()
    writerInst.terminate()
 
    for tmpFile in tempFilesList:
        os.remove(tmpFile)

if __name__ == "__main__":
    #(options, args) = setupOptions()
    #setupDebug( options.debug1, options.debug2 )

    #testing()

    main()


