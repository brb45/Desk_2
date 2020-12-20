# limits.py

import fnmatch

#class LimitExpr_t:
#    def __init__(self, flow, test ):
#        self.flow = flow
#        self.test = test
#        self.s = ""
#    def getLimit(self, expr):
#        # expr is something like " = TX_POWER_DBM - 1.5"
#        result = ""
#        # strip off the equals
#        expr = expr.lstrip("= ")
#        paramNames = self.flow.getParamOrder()
#        # set input parameters as variables in this scope
#        for i in range( len( paramNames ) ):
#            try:  
#                cmd = "%s = %f"%(paramNames[i],float(self.test[i]))
#            except:
#                cmd = "%s = \"%s\""%(paramNames[i],self.test[i])
#            exec( cmd )
#        # evaluate the expression to compute the limit value
#        result = eval( expr )
#        return str(result)
    
def evalExpr_prev( flow, test, expr):
    # expr is something like " = TX_POWER_DBM - 1.5"
    result = ""
    # strip off the equals
    expr = expr.lstrip("= ")
    paramNames = flow.getParamOrder()
    # set input parameters as variables in this scope
    for i in range( len( paramNames ) ):
        try:  
            cmd = "%s = %f"%( paramNames[i], float( test[i]) )
        except:
            cmd = "%s = \"%s\""%( paramNames[i], test[i])
        exec( cmd )
    # evaluate the expression to compute the limit value
    result = eval( expr )
    return str( result )

def evalExpr( testParams, expr):
    # expr is something like " = TX_POWER_DBM - 1.5"
    result = ""
    # strip off the equals
    expr = expr.lstrip("= ")
    #paramNames = flow.getParamOrder()
    # set input parameters as variables in this scope
    for (param,value) in testParams.iteritems():
        try:  
            cmd = "%s = %f"%( param, float( value) )
        except:
            cmd = "%s = \"%s\""%( param, value )
        exec( cmd )
    # evaluate the expression to compute the limit value
    result = eval( expr )
    return str( result )

#class LimitMap_t:
#    def __init__( self, flow, test ):
#        self.flow = flow
#        self.test = test
#        self.s = ""
#    def extractParams( self, s ):
#        plist = s.split(',')
#        self.params = plist
#    def append(self, s ):
#        self.s = self.s + s
#        
#    def findmap( self, maplist, valuelist ):
#        for amap in maplist:
#            for i in range(0,len(valuelist)):
#                value = valuelist[i]
#                pattern = amap[0][i]
#                if fnmatch.fnmatch( value, pattern ):
#                    # matched, move to the next param
#                    continue    
#                # no match, skip to the next patterns
#                break
#            else:
#                # all param values matched the patterns, so we can use this value
#                return amap[1]
#        # could not match any patterns...
#        return ""
#
#    def getLimit( self ):
#        #paramNames = self.s.split(")")[0].replace(" ","").lstrip(" (").split(",")
#        self.s = self.s.replace(" ","")
#        paramNames = self.s.split(")")[0].lstrip(" (").split(",")
#        testParams = dict( zip( self.flow.getParamOrder(), self.test ) )
#        
##       for i in range( len( paramNames ) ):
##            try:  
##                cmd = "%s = %f"%(paramNames[i],float( testParams[ paramNames[i] ]))
##            except:
##                cmd = "%s = \"%s\""%(paramNames[i], testParams[ paramNames[i] ])
##            exec( cmd )
#        valuelist = []
#        for i in range( len( paramNames ) ):
#            valuelist.append( str( testParams[ paramNames[i]] ) )
#        maplist = []
#        exprList = self.s.split(")")[1].split(";")
#        for expr in exprList:
#            if "=" in expr:
#                (params,value) = expr.split("=")
#                maplist.append( [ params.split(","), value ] )
#                # e.g., (OFDM-6,2424)=-15; -> [ ["OFDM-6", "2424"], "-15" ]
#        # now look up limit value in the map we just created
#        limit = self.findmap( maplist, valuelist )
#        
#        # limit could be an expression
#        #limitExpr = LimitExpr_t( self.flow, self.test )
#        #limit = limitExpr.getLimit( limit )
#        limit = evalExpr( self.flow, self.test, limit )
#        return limit
       
class LimitMap_t:
    def __init__( self, testParams ):
        self.testParams = testParams
        self.s = ""
    def extractParams( self, s ):
        plist = s.split(',')
        self.params = plist
    def append(self, s ):
        self.s = self.s + s
        
    def findmap( self, maplist, valuelist ):
        for amap in maplist:
            for i in range(0,len(valuelist)):
                value = valuelist[i]
                pattern = amap[0][i]
                if fnmatch.fnmatch( value, pattern ):
                    # matched, move to the next param
                    continue    
                # no match, skip to the next patterns
                break
            else:
                # all param values matched the patterns, so we can use this value
                return amap[1]
        # could not match any patterns...
        return ""

    def getLimit( self ):
        #paramNames = self.s.split(")")[0].replace(" ","").lstrip(" (").split(",")
        self.s = self.s.replace(" ","")
        paramNames = self.s.split(")")[0].lstrip(" (").split(",")
        
        valuelist = []
        for i in range( len( paramNames ) ):
            valuelist.append( str( self.testParams[ paramNames[i]] ) )
        maplist = []
        exprList = self.s.split(")")[1].split(";")
        for expr in exprList:
            if "=" in expr:
                (params,value) = expr.split("=")
                maplist.append( [ params.split(","), value ] )
                # e.g., (OFDM-6,2424)=-15; -> [ ["OFDM-6", "2424"], "-15" ]
        # now look up limit value in the map we just created
        limit = self.findmap( maplist, valuelist )
        
        # limit could be an expression
        #limitExpr = LimitExpr_t( self.flow, self.test )
        #limit = limitExpr.getLimit( limit )
        if limit != "":
            limit = evalExpr( self.testParams, limit )
        return limit

def get_EVM_AVG_DB_limit( rate ):
    return {
              "OFDM-6"  : "-5",
              "OFDM-9"  : "-8",
              "OFDM-12" : "-10",
              "OFDM-18" : "-13",
              "OFDM-24" : "-16",
              "OFDM-36" : "-19",
              "OFDM-48" : "-22",
              "OFDM-54" : "-25",
              "DSSS-1"  : "-10",
              "DSSS-2"  : "-10",
              "CCK-5_5" : "-10",
              "CCK-11"  : "-10",
              "MCS0"    : "-5",
              "MCS1"    : "-10",
              "MCS2"    : "-13",
              "MCS3"    : "-16",
              "MCS4"    : "-19",
              "MCS5"    : "-22",
              "MCS6"    : "-25",
              "MCS7"    : "-28",
              "MCS8"    : "-5",
              "MCS9"    : "-10",
              "MCS10"   : "-13",
              "MCS11"   : "-16",
              "MCS12"   : "-19",
              "MCS13"   : "-22",
              "MCS14"   : "-25",
              "MCS15"   : "-28",
              "MCS16"   : "-5",
              "MCS17"   : "-10",
              "MCS18"   : "-13",
              "MCS19"   : "-16",
              "MCS20"   : "-19",
              "MCS21"   : "-22",
              "MCS22"   : "-25",
              "MCS23"   : "-28",
           }.get(rate, "-5")
