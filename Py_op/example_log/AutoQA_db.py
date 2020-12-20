import mysql.connector

conn = mysql.connector.connect(host="192.168.14.254",user="gdlocal",passwd="gdlocal",db="AutoQA")
cur = conn.cursor()
dut_ID = "4360"
status = 1
uquery =  ("UPDATE AutoQAStations SET status=0 WHERE DUT=%s")
uquery =  ("UPDATE AutoQAStations SET status=%s WHERE DUT=%s")
cur.execute(uquery,(dut_ID,))
conn.commit()

squery = ("SELECT systemIP, DUT FROM AutoQAStations WHERE DUT=%s")
squery1 = ("SELECT DUT, systemIP FROM AutoQAStations WHERE nup=%s AND testerMounted=%s ORDER BY timestampupdated DESC LIMIT 3")
#note timestampupdated is a column name
# LIMIT 3 mean only show upto 3

cur.execute(squery,(dut_ID,))
cur.fetchall()

squery1 = ("SELECT DUT, systemIP FROM AutoQAStations WHERE nup=%s AND testerMounted=%s ORDER BY dateTime DESC LIMIT 1")
tester="IQ2800"
nup="0,1,2,3"
cur.execute(squery1, (nup, tester))
cur.fectchall()

cur.execute("Select VERSION()")
#[('5.6.12',)] is mysql version

sql = """CREATE TABLE TempResult (
   LogName  CHAR(20) NOT NULL,
   failCount  CHAR(20)
    )"""
cur.execute(sql)
conn.commit() # no changes can be reversed
conn.rollback() # use before commit

sql = "INSERT INTO TempResult (LogName,failCount) VALUES ( '%s','%s')" %("regression_test","10")
sql = "INSERT INTO TempResult (LogName,failCount) VALUES ( '%s','%s')" %("regression_test","10")
testname = "mimo"
run = 20
sql = "INSERT INTO TempResult (LogName,failCount) VALUES ( '%s','%s')" %(testname,run)
//sql = "INSERT INTO TempResult (LogName,failCount) %s',%s)"
sql = "SELECT * FROM TempResult WHERE failCount = '%s'" % (10)

>>> sql = "SELECT * From TempResult WHERE failCount = %s"
>>> failCount = 10
>>> cur.execute(sql,(failCount,))

#sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)


"""
To find files in immediate subdirectories: single '*' is for immediate subdiroor
configfiles = glob.glob(r'C:\Users\sam\Desktop\*\*.txt')
C:\Users\jsun\Documents\PyProj\file_op\logoutput\log1.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\log2.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\log3.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\temp\log3.txt

For a recursive version that traverse all subdirectories, you could use ** and pass recursive=True since Python 3.5:
configfiles = glob.glob(r'C:\Users\sam\Desktop\**\*.txt', recursive=True)
"C:\Program Files\Python36\python.exe" C:/Users/jsun/Documents/PyProj/file_op/file_test.py
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\LogRXRX\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\LogRXRX\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\LogRXTX\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\LogRXTX\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\Log_TXRX\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\Log_TXRX\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\Log_TXTX\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUMU\Log_TXTX\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUSU\LogMUSU_RX_RXTX\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUSU\LogMUSU_RX_RXTX\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUSU\MUSU_TX_TXRX\logCurrent.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUSU\MUSU_TX_TXRX\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\MUSU\MUSU_TX_TXRX\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\SUMU\LogSUMU\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\SUMU\LogSUMU\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\SUSU\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\IQfact+_BRCM_4378_MPS_4.0.0.43\SUSU\Log_all.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\log1.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\log2.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\log3.txt
C:\Users\jsun\Documents\PyProj\file_op\logoutput\logOutput.txt
C:\Users\jsun\Documents\PyProj\file_op\temp\log3.txt



filesrch = os.path.join(os.getcwd(),"**","*.txt")
glob.glob(filesrch, recursive=True)

from glob import glob
import os
schfile = os.path.join(os.getcwd(),"**","*.txt")
a = glob(schfile,recursive=True)
for i in a:
    print(i)
"""

