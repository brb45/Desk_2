# readtemplate.py

import zipfile

templatesZipFile_g = "templates.zip"
#templatesZipFile_g = "abd.zip"

def readtemplate( tFileName ):
    try:
        z = zipfile.ZipFile( templatesZipFile_g, "r" )
        print ">>>> reading from zipped template file....."
        data = z.read( tFileName )
        z.close()
    except IOError:
        print ">>>> reading from regular template file....."
        f = open( tFileName, "r" )
        data = f.read()
        f.close()
    lines = data.splitlines()
    return lines

def printlines( lines ):
    for line in lines:
        print "line: ",line

if __name__ == "__main__":
    printlines( readtemplate( "templates/iqlite/WIFI/TX_VERIFY_EVM.txt" ))
    #printlines( readtemplate( "templates/short/BT/TX.txt" ))
    #printlines( readtemplate( "templates/push/WIFI/tx_test.txt" ))

