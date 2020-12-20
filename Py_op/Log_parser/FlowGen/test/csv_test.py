import csv
def readCsv(fname, dialect=None):
    """ Uses csv reader to get data from csv to dict """

    try:
        fh = open(fname, 'r')
        if dialect is None:
            reader = csv.reader(fh)
        else:
            reader = csv.reader(fh, dialect=dialect)
        keys = reader.next()
        data = {}
    except:
        return

    # Make keys even if no data
    for key in keys:
        data[key] = []

    #self.clear()

    while True:
        try:
            d = dict(zip(keys, reader.next()))
            self.append(d)
        except StopIteration:
            break
        except Exception as e:
            fh.close()
            raise Exception(str(e))

    fh.close()

if __name__ == "__main__":
    fname = "example1_wifi.csv"
    readCsv(fname, dialect=None)
