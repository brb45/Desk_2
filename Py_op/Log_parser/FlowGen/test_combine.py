def combinations(list):
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
    combos = combinations(plist)
    print (type(combos))
    # we don't sort anymore because reversing works better
    #combos.sort()
    for tlist in combos:
        tlist.reverse()
    return combos

def main():
    rawParamList = [[2412, 2417, 2422], ['OFDM_6', 'OFDM_12'],
            ['TX_VERIFY_EVM', 'TX_VERIFY_MASK', 'RX_VERIFY_PER' ], ['15.2', '14.7'],
            ['(0,1,0,0)', '(1,0,0,0)']]
    combos = getParamCombinations(rawParamList)
    print (combos)
    d = {1:'a',2:'b'}
    copied = d.copy()
    d[1]='z'
    copied[2]="H"
    print (d)
    print (copied)
    #shallow copy vs deep copy
    xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sh_copy_xs = list(xs)
    xs.append(['new element']) #[[1, 2, 3], [4, 5, 6], [7, 8, 9], ['new element']]
    #sh_copy_xs: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    xs[1][0] = 'X'#[[1, 2, 3], ['X', 5, 6], [7, 8, 9], ['new element']]
    #sh_copy_xs: [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
    print (xs)        #[[1, 2, 3], ['YY', 5, 6], [7, 8, 9], ['new element']]
    print (sh_copy_xs)#[[1, 2, 3], ['YY', 5, 6], [7, 8, 9]]
    sh_copy_xs.append("new copy")
    #sh_copy_xs: [[1, 2, 3], ['X', 5, 6], [7, 8, 9], 'new copy']
    #xs: [[1, 2, 3], ['X', 5, 6], [7, 8, 9], ['new element']]
    import copy
    ys = copy.copy(xs) #shallow copy
    deepYs = copy.deepcopy(xs) #deep copy

if __name__ == "__main__":
    main()