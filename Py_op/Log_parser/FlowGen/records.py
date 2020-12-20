

""" Provides storing and manipulation of 'records' (dictionaries) """

### NOTE: THIS IS A COPY OF THE FILE FOUND IN THE TEST_AUTOMATION SVN TREE ###
###     AVOID MODIFYING THIS FILE!!!    

# Python modules
import os
import re
import csv
import logging

#--------------------------------------------------------------------
#  LOCAL
#--------------------------------------------------------------------

def sortDictKeys(dictkeys, order=[], skip=[]):
    """
    Returns the sorted list of dict keys

    Inputs:
       dictkeys -- (list) Dictionary Key List to sort on
       order    -- (list) Specified order for some keys
       skip     -- (list) Skip keys in this list
    """

    # Assign all elements Max Order Number
    hash_order = dict( [(k, len(dictkeys)) for k in dictkeys] )

    # Assign Order Num, if specified by order
    for i in range(len(order)):
        hash_order[order[i]] = i

    for key in skip:
        dictkeys.remove(key)

    # Use Order Number to Sort
    dictkeys.sort(lambda x,y: cmp(hash_order[x], hash_order[y]))

    return dictkeys



def appendDict(data, d):
    """
    Appends a record (dict) onto a dictionary of lists.

    Inputs:
        data  -- dictionary of lists
        d     -- dictionary of values to append

    Notes:
    - Maintains length of all lists by appending or inserting None
    """

    # Verify dict lists are same length
    length=0
    for key1 in data:
        for key2 in data:
            if (len(data[key1]) != len(data[key2])):
                raise Exception("Length mismatch in data lists")
        length = len(data[key1])
        break

    for key in d:
        # Found new key, insert None's
        if key not in data:
            data[key] = [None] * length
        data[key].append(d[key])

    # Push None for Missing Data
    for key in data:
        if len(data[key]) <= length:
            data[key].append(None)

    return data



class RecordDB(dict):
    """
    RecordDB provides an object to store data into a 'record' database. A
    'record' consists of a Python dict, and the RecordDB class is composed of
    a dictionary of lists. This class supports the data to be converted and
    manipulated for presentation.
    """

    def __init__(self, fname=None, verbose=0, dialect=None):

        self._order = []
        self.verbose = verbose

        if verbose:
            logging = logging.getLogger('records')

        if fname is not None:
            self.readCsv(fname, dialect)


    def __len__(self):
        """ Returns the database length """

        if self.keys():
            return len(self[self.keys()[0]])  # length of any list
        else:
            return 0


    def __add__(self, value):
        """ Adds RecordDB's by append records to self """

        if not isinstance(value, dict):
            raise TypeError("Cannot add RecordDB to type %s" %str(value))

        if not self._isValidDb(value):
            raise Exception('Summed value is not the correct format')

        temp = self

        if len(value.keys()) > 0:
            dlen = len(value[value.keys()[0]])

            for i in range(dlen):

                rec = dict((key, value[key][i]) for key in value)
                temp.append(rec)

        return self


    def __eq__(self, value):
        """ Clears current keys/values and takes on value """

        if self._isValidDb(value):
            self.clear(); self.update(value)

    def _isValidDb(self, db):
        """ Determines if the dict has values that are lists of the same length """

        for key in db:
            if not isinstance(db[key], list): return False

        values = map(len, db.values())
        return not filter(lambda x: x != values[0], values)

    def append(self, rec):
        """ Appends a record (dict) onto a dictionary of lists """

        if self.verbose:
            logging.info('-' * 65)
            logging.info('New Record:')
            for key in sorted(rec):
                logging.info('    %s = %s' % (key, rec[key]))
            logging.info('-'*65)

        if self.keys():
            length = len(self)
        else:
            length = 0
            
        for key in rec:
            # Found new key, insert None's
            if key not in self:
                self[key] = [None] * length
            self[key].append(rec[key])

        # Push None for Missing Data
        for key in self:
            if len(self[key]) <= length:
                self[key].append(None)

    def pop(self, index):
        """ Returns the record (dict) for the provided index """

        return dict([(key, self[key].pop(index)) for key in self])

    def errorCheck(self, thresh, x_data, key):
        """ Uses errorCheck function to test limits """

        return errorCheck(self, thresh, x_data, key)

    def readCsv(self, fname, dialect=None):
        """ Uses csv reader to get data from csv to dict """

        try:
            fh     = open(fname, 'r')
            if dialect is None:#Not the case
                reader = csv.reader(fh)
            else:
                #print("dialect is ", dialect)#('dialect is ', 'flowgen')
                #print("fname is ",fname)#('fname is ', 'input\\example1_wifi.csv')
                reader = csv.reader(fh, dialect=dialect)
            keys = reader.next()
            print("keys is",keys)
            #('keys is', ['TECHNOLOGY', 'DATA_RATE', 'FREQ_MHZ', 'TEST', 'TX_POWER_DBM'])
            data = {}
        except:
            return

        # Make keys even if no data
        for key in keys:
            data[key] = []

        self.clear()
        line = 0
        while True:
            try:

                d = dict(zip(keys, reader.next()))
                print("line is ", line)
                line +=1
                """
                for key, value in d.items():
                    print(key," --> ", value)
                    print("\n")
                    #print each line of csv file,except title line
                """
                self.append(d)
            except StopIteration:
                break
            except Exception as e:
                fh.close()
                raise Exception(str(e))
        """
        print(d['DATA_RATE'])
        for key,val in d.items():
            print(key, val)
        print('next')
        ('FREQ_MHZ', '')
        ('DATA_RATE', 'OFDM-54')
        ('TECHNOLOGY', '')
        ('TEST', '')
        ('TX_POWER_DBM', '')
        """

        fh.close()

    def appendCsv(self, fname):
        """ Appends the CSV data to the current dict
            Seems not being used
        """

        fh     = open(fname, 'r')
        reader = csv.reader(fh)
        keys   = reader.next()
        data = {}

        while True:
            try:
                d = dict(zip(keys, reader.next()))
                """
                
                for key, value in d.items():
                    print(key, value)
                    print("are we even here")
                """

                self.append(d)
            except StopIteration:
                break
            except (e, v):
                fh.close()
                raise Exception('%s: %s' %(e, v))

        fh.close()

    def writeCsv(self, fname, order=[], skip=[]):
        """ Uses dictToCsv function to write to csv file """

        if '.csv' not in fname:  fname += '.csv'

        fh = open(fname, 'wb')

        writer = csv.writer(fh)
        keys   = sortDictKeys(self.keys(), order, skip)
        maxlen = max([len(self[key]) for key in keys])

        writer.writerow(keys)
        print("We are at def writeCsv(self, fname, order=[], skip=[]):")
        for i in range(maxlen):

            # Create a row, '' if no value exists
            row = []
            for key in keys:
                if len(self[key]) > i:  row.append(self[key][i])
                else:                   row.append('')

            writer.writerow(row)

        fh.close()

    def split(self, split_key):
        """ Splits RecordDB across key's unique values. Returns a dictionary of RecordDB's """
        print("We are at split(self,split_key)")
        temp = {}

        for i in range(len(self)):

            new_key = str(self[split_key][i])
            temp.setdefault(new_key, RecordDB())

            for key in self:
                temp[new_key].setdefault(key, []).append(self[key][i])

        return temp

    def iterrecords(self):
        """ Iterates each record in the record database """

        for i in range(len(self)):
            yield dict([(key, self[key][i]) for key in self])

    def records():
        """ Property to return the records as a list """

        def fget(self):
            return [rec for rec in self.iterrecords()]

        def fset(self, value):
            self.clear()
            for rec in value:
                self.append(rec)

        return locals()

    records = property(**records())

    def getRecordTable(self, order=[], skip=[], header=1):
        """
        Returns a list of lists to represent the db table.

        Inputs:
            order  -- option to set the order of the keys
            skip   -- option to skip keys
            header -- option to add the header to table
        """

        # Order the keys
        keys = sortDictKeys(self.keys(), order, skip)

        data = []
        for key in keys:
            if header:  data.append([key] + self[key])
            else:       data.append(self[key])

        return data

    ''' TODO
    def setOrder(self, order):
        """
        Sets an order for all functions in processing the keys. This is overridden
        if the argument input specifies an order.

        Inputs:
            order -- list of keys (strings)
        """

        self._order = order
    '''

class StackDB(RecordDB):
    """ A database that stacks data without inserted/appended None values """

    def append(self, rec):
        for key, val in rec.items():
            if not ((val is None) or (val == '')):
                self.setdefault(key, []).append(val)

    def __len__(self):
        """ Returns the database largest list length """

        if self.keys():
            return max([len(self[key]) for key in self])
        else:
            return 0

    def __add__(self, value):
        """ Adds RecordDB's by append records to self """

        if not isinstance(value, dict):
            raise TypeError("Cannot add %s to type %s" % (self.__class__.__name__, str(value)))

        for (key, values) in value.items():
            self.setdefault(key, []).extend(values)

        return self



