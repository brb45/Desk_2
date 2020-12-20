import mysql.connector
import shutil
import os
import datetime
import os.path
import zipfile
import subprocess
import smtplib
import time
import textwrap
import subprocess


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from cgi import escape
from email.header import Header

import simplejson as json
from pprint import pprint

MACHINE_ID = "AUTO_QA_BRCM4378"
STATUS_STANDBY = "STANDBY"
STATUS_INPROCESS = "IN_PROCESS"
STATUS_DONE_OK = "OK"
STATUS_DONE_ERROR = "ERROR"
STATUS_AUTO_QA_DONE = "AUTO_QA_DONE"

# copy .zip to the following folder, for local installation
QA_DOWNLOAD_PATH = "C:\\Li\Auto_QA\\downloads\\"
QA_RELATED_PATH = "C:\\Li\\Auto_QA\\Automation_Related\\BRCM4378\\"
QA_FILE_MULTI_DUT = "IQfact_MultiDUT.ini"
QA_FILE_PATHLOSS_DUT_1 = "path_loss_dut1.csv"
QA_FILE_PATHLOSS_DUT_2 = "path_loss_dut2.csv"
QA_FILE_FLOW = "Murata_flow_limits_DUT1_auto_QA.txt"

LOG_2_JSON_EXE = "log2json.exe"
JSON_RESULT_SUMMARY = "runlist"
JSON_NUM_INPUTS = "inputs"
JSON_NUM_OUTPUTS = "outputs"
JSON_DETAIL_FILE = "log_all_detail.json"
JSON_SUMMARY_FILE = "log_all_summary.json"

# QA_FILE_FLOW = "4378_develop.txt"
QA_DEVELOP_FLOW = "4378_develop.txt"

TEST_FLOW_UPDATED = "TEST_FLOW_UPDATED.txt"

QA_TMP_FOLDER = "C:\\Li\\temp\\BRCM4378\\"


COL_WS_NAME = "WorkStationName"
COL_STATUS = "JobStatus"
COL_MISC = "Misc"

DUT_1, DUT_2 = "dut_1", "dut_2"

config = {
    'user': 'AutoQAWorker',
    'password': 'Litepoint1',
    # 'host': 'iqfactsrv01',
    'host': '192.168.2.141',    
    'database': 'autoqa',
    'raise_on_warnings': True
}

DB_TABLE = "work"

LP_PATH = "C:\\LitePoint\\IQfact_plus\\"

IQRAMP_REPORT_BUILDER = "reportBuildr.bin"
IQRAMP_BUILDER_FULL_PATH = QA_RELATED_PATH + IQRAMP_REPORT_BUILDER
IQRAMP_TEMPLATE_FULL_PATH = QA_RELATED_PATH + "IQRamp_template_4378.json"

Sender = "DataDrivenQA_Brcm4378@litepoint.com"
Recipients = ['li.wu@litepoint.com', 'david.yin@litepoint.com', 'kaiyun.cui@litepoint.com', 'jian.sun@litepoint.com', \
                'buddy.erhardt@litepoint.com', 'qing.chen@litepoint.com', \
                'yueqian.li@litepoint.com', 'kunal.bharucha@litepoint.com' , \
                'navya.patibandla@litepoint.com', 'betzhang@litepoint.internal', \
                    'vivek.patel@litepoint.com','victor.chang@litepoint.com']

# Recipients = ['li.wu@litepoint.com']
QA_DUT_IP_ARRAY = ["10.201.10.118", "10.201.10.115"]
QA_DUT_USER_ARRAY = ["root", "root"]
QA_DUT_PASSWORD_ARRAY = ["brcm123$", "brcm123$"]
QA_DUT_PATH_ARRAY = ["//root//FW_A1//", "//root//FW_A1//"]
QA_DUT_CMD_KILL = "kill  `pgrep wl_server`"
QA_DUT_CMD_RELOAD = "./load.sh >/dev/null"
# QA_DUT_CMD_RELOAD = "./load.sh >/dev/null &"
QD_DUT_CMD_CHECK_WL_SERVER = "ps -a | grep wl_server_"

def prepare_DUT():
    # check plink.exe exists
    PLINK_FULL_PATH = QA_RELATED_PATH + "plink.exe"

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    if (os.path.isfile(PLINK_FULL_PATH)):
        print ("found plink.exe at ", PLINK_FULL_PATH)
    else:
        print ("Can not found plink.exe", PLINK_FULL_PATH)
        return -1

    for DUT_ID in [1,2]:
        DUT_IP = QA_DUT_IP_ARRAY[DUT_ID-1]
        DUT_USER = QA_DUT_USER_ARRAY[DUT_ID-1]
        DUT_PWD = QA_DUT_PASSWORD_ARRAY[DUT_ID-1]
        DUT_PATH = QA_DUT_PATH_ARRAY[DUT_ID-1]
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
        print ("DUT_IP = ", DUT_IP, " DUT_USER = ", DUT_USER, " DUT_PWD = ", DUT_PWD, " DUT_PATH = ", DUT_PATH)

        # kill wl_server*
        # CMD = "echo y | "
        # CMD += PLINK_FULL_PATH + " -ssh " + DUT_USER + "@" + DUT_IP + " -P 22 " + "-pw " + DUT_PWD + " -C " + "killall -9 wl_server*" 
        CMD = PLINK_FULL_PATH + " -ssh " + DUT_USER + "@" + DUT_IP + " -P 22 " + "-pw " + DUT_PWD + " -C " + QA_DUT_CMD_KILL
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
        print ("CMD = ", CMD)

        res = os.system(CMD)


        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
        print ("CMD res = ", res)

        #load.sh
        # CMD = "echo y | "
        CMD = PLINK_FULL_PATH + " -ssh " + DUT_USER + "@" + DUT_IP + " -P 22 " + "-pw " + DUT_PWD + " -C " + "\"" +  " cd " + DUT_PATH + " ; " + QA_DUT_CMD_RELOAD + "\""
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
        print ("CMD = ", CMD)        
    
        res = os.system(CMD)

        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
        print ("CMD res = ", res)

    # sleep 30 seconds to wait for DUTs ready
    time.sleep(30)

    #might need check DUT status; Will do this later
    return 0

def retrieve_work_from_db():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = "select * from " + DB_TABLE + " WHERE " + COL_WS_NAME + " = '" + MACHINE_ID + "' AND " + COL_STATUS + " = '" + STATUS_STANDBY + "'"

        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
        print ("query = " + query)

        cursor.execute(query)
        result = cursor.fetchall()
        # cursor.fetchone()


        cnx.close()
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
        print ("cursor.rowcount = ", cursor.rowcount)

        return cursor.rowcount, result
    except mysql.connector.Error as err:
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")        
        print("Something went wrong: {}".format(err))

        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")  
        print ("when database error happends, sleep 60 seconds in case db needs recovery")
        # sleep 60 seconds
        time.sleep(60)

        return 0,""

def update_compare_flow(path_bin):
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
    print ("update_compare_flow called, path_bin = ", path_bin)

    cur_path = os.getcwd()
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
    print ("cur_path = ", cur_path)

    if (os.path.isdir(path_bin)):
        print (path_bin + " found")
    else:
        print ("path_bin not valid path, ", path_bin)
        os.chdir(cur_path)
        return -1



    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
    print ("switch to path_bin = ", path_bin)
    os.chdir(path_bin)

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
    if (os.path.isfile(QA_FILE_FLOW)):
        print ("found QA_FILE_FLOW, ", QA_FILE_FLOW)
    else:
        print ("Copy " + QA_RELATED_PATH + QA_FILE_FLOW  + " to installed bin")
        shutil.copyfile(r"{}".format(QA_RELATED_PATH + QA_FILE_FLOW ),
                        QA_FILE_FLOW )        

    # check QA flow file after copy
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
    if (os.path.isfile(QA_FILE_FLOW)):
        print ("after copy found QA_FILE_FLOW, ", QA_FILE_FLOW)
    else:
        print ("after copy, could not find QA_FILE_FLOW, ", QA_FILE_FLOW)
        os.chdir(cur_path)
        return -1

    updated_flow_file = TEST_FLOW_UPDATED

    # just remove it, in case exists
    if (os.path.isfile(updated_flow_file)):  
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
        print (updated_flow_file + " exists, remove it first")
        os.remove(updated_flow_file)


    cmd = "IQfactRun_Console.exe -read " + QA_FILE_FLOW + " -saveas " + updated_flow_file + " –writereturns"
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("run cmd, ", cmd)
    res = os.system(cmd)

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("run cmd res = ", res)

    # check updated_flow_file
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
    if (os.path.isfile(updated_flow_file)):
        print ("after execution, generated updated_flow_file , ", updated_flow_file)
    else:
        print ("after execution, no updated_flow_file , ", updated_flow_file)
        os.chdir(cur_path)
        return -1

    # end
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
    print ("switch back to cur_path = ", cur_path)
    os.chdir(cur_path)

    return 0,updated_flow_file


def perform_one_task(command):

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
    print ("perform_one_task called, command = ", command)

    idx_ID, idx_station, idx_package, idx_status = 0, 1,2,3
    res = -1

    ROW_LENTH = 4

    if len(command) < ROW_LENTH:
        print ("wrong command")
        return -1

    job_id = command[idx_ID]
    job_station = command[idx_station]
    job_status = command[idx_status]
    job_package = command[idx_package]

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("job_id = ", job_id)
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("job_station = ", job_station)
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("job_status = ", job_status)
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("job_package = ", job_package)

    base_file = os.path.basename(job_package)

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("base_file = ", base_file)
    # print ("r.format(job_package = ", r"{}".format(job_package)

    # create folders if not exist
    if not os.path.exists(QA_DOWNLOAD_PATH):
        os.makedirs(QA_DOWNLOAD_PATH)

    if not os.path.exists(QA_RELATED_PATH):
        os.makedirs(QA_RELATED_PATH)

    # check source file exists
    if (os.path.isfile(job_package)):
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
        print ("this is a valid source package")

        #Now prepareDUT when there is a valid package
        res = prepare_DUT()

        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
        print ("prepare_DUT res = ", res)

        # remove destination
        # print ("in case destination exists, remove it, res = ", res)
        if (os.path.isfile(QA_DOWNLOAD_PATH + base_file)):
            os.remove(QA_DOWNLOAD_PATH + base_file)

        shutil.copyfile(r"{}".format(job_package), QA_DOWNLOAD_PATH + base_file)

        PACK_NAME = ""
        if (os.path.isfile(QA_DOWNLOAD_PATH + base_file)):
            # print ("copy succesfully")
            with zipfile.ZipFile(QA_DOWNLOAD_PATH + base_file, 'r') as zip_ref:

                PACK_NAME = os.path.splitext(base_file)[0]
                UNZIP_FOLDER_PATH = QA_DOWNLOAD_PATH + PACK_NAME
                # print ("UNZIP_FOLDER_PATH = ", UNZIP_FOLDER_PATH)
                zip_ref.extractall(UNZIP_FOLDER_PATH)

            #in case packages already installed, remove it first

            shutil.rmtree(LP_PATH + PACK_NAME, ignore_errors=True)

            #now install package, U
            cmd = UNZIP_FOLDER_PATH + "\\IQfact_plus\\setup.exe /S"
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            print ("cmd = ", cmd)

            res = os.system(cmd)
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            print ("installation re = ", res)

            if (res == 0):
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("installation success")

                #check installed folder exists or not
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                if (os.path.isdir(LP_PATH + PACK_NAME + "\\bin\\")):
                    print (LP_PATH + PACK_NAME + "\\bin\\" + " found")

                    # copy Multi Duts ini
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("Copy " + QA_RELATED_PATH + QA_FILE_MULTI_DUT + " to installed bin")
                    shutil.copyfile(r"{}".format(QA_RELATED_PATH + QA_FILE_MULTI_DUT),
                                    LP_PATH + PACK_NAME + "\\bin\\" + QA_FILE_MULTI_DUT)


                    # copy pathloss dut1
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("Copy " + QA_RELATED_PATH + QA_FILE_PATHLOSS_DUT_1 + " to installed bin")
                    shutil.copyfile(r"{}".format(QA_RELATED_PATH + QA_FILE_PATHLOSS_DUT_1),
                                    LP_PATH + PACK_NAME + "\\bin\\" + QA_FILE_PATHLOSS_DUT_1)

                    # copy pathloss dut2
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("Copy " + QA_RELATED_PATH + QA_FILE_PATHLOSS_DUT_2 + " to installed bin")
                    shutil.copyfile(r"{}".format(QA_RELATED_PATH + QA_FILE_PATHLOSS_DUT_2),
                                    LP_PATH + PACK_NAME + "\\bin\\" + QA_FILE_PATHLOSS_DUT_2)

                    # copy flow
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("Copy " + QA_RELATED_PATH + QA_FILE_FLOW  + " to installed bin")
                    shutil.copyfile(r"{}".format(QA_RELATED_PATH + QA_FILE_FLOW ),
                                    LP_PATH + PACK_NAME + "\\bin\\" + QA_FILE_FLOW )

                    # copy develop flow, for debug purpose
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("Copy " + QA_RELATED_PATH + QA_DEVELOP_FLOW  + " to installed bin")
                    shutil.copyfile(r"{}".format(QA_RELATED_PATH + QA_DEVELOP_FLOW ),
                                    LP_PATH + PACK_NAME + "\\bin\\" + QA_DEVELOP_FLOW )

                    # change dir
                    os.chdir(LP_PATH + PACK_NAME + "\\bin\\")

                    #update test flow and compare it
                    res_update_flow, res_update_flow_name = update_compare_flow (LP_PATH + PACK_NAME + "\\bin\\")
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("res_update_flow = ", res_update_flow, " res_update_flow_name = ", res_update_flow_name)
  
                    if res_update_flow != 0:
                        res_update_flow_name = ""

                    #run
                    cmd = "IQfactRun_Console.exe -silent -multidut " + QA_FILE_MULTI_DUT + " -run " + QA_FILE_FLOW + " -exit"
                    # cmd = "IQfactRun_Console.exe -silent -multidut " + QA_FILE_MULTI_DUT + " -run " + res_update_flow + " -exit"


                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")

                    print ("run cmd, ", cmd)
                    res = os.system(cmd)
                    # subprocess.call(cmd)


                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("run cmd res = ", res)

                    # setup DES_FOLDER 
                    DES_FOLDER = "\\\\lphqfiler1\Public\Business Development\Public\BD_QA\QA_Automation\AUTO_QA_BRCM4378\\" + \
                                datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + \
                                "\\" + PACK_NAME + "\\" ;
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("DES_FOLDER = ", DES_FOLDER);

                    # copy log file to \\lphqfiler1\Public\Business Development\Public\BD_QA\QA_Automation\AUTO_QA_BRCM4378\
                    for dut_x in [DUT_1, DUT_2]:
                        LOG_PATH_DUT_X = LP_PATH + PACK_NAME + "\\bin\\" + dut_x

                        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ") 
                        if (os.path.isdir(LOG_PATH_DUT_X)):
                            print ("log folder exists, ", LOG_PATH_DUT_X)

                            SRC_FOLDER = LOG_PATH_DUT_X
                            IGNORE_PATTERNS = ('*.iqvsa')

                            try:
                                shutil.copytree(SRC_FOLDER, DES_FOLDER+dut_x, ignore=shutil.ignore_patterns(IGNORE_PATTERNS))
                                # Directories are the same
                            except shutil.Error as e:
                                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                                print('Directory not copied. Error: %s' % e)
                                # Any error saying that the directory doesn't exist
                            except OSError as e:
                                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                                print('Directory not copied. Error: %s' % e)

                        else:
                            print ("log folder DOES NOT exists, ", LOG_PATH_DUT_X)
                            return -1

                    # copy updated flow file to \\lphqfiler1\Public\Business Development\Public\BD_QA\QA_Automation\AUTO_QA_BRCM4378\
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("now check file exists or not ,  ", res_update_flow_name, " exists = ", os.path.isfile(res_update_flow_name));

                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("now check FOLDER exists or not ,  ", DES_FOLDER, " exists = ",  os.path.isdir(DES_FOLDER));

                    if (os.path.isfile(res_update_flow_name)):
                        try:
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                            print ("now copy  ", res_update_flow_name, " to ", DES_FOLDER+res_update_flow_name);
                            shutil.copy2(res_update_flow_name, DES_FOLDER+res_update_flow_name)
                        except shutil.Error as e:
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                            print('updated flow file not copied. Error: %s' % e)
                            # Any error saying that the directory doesn't exist
                        except OSError as e:
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                            print('updated flow file not copied. Error: %s' % e)

                    else:
                        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                        print ("not a valid file,  ", res_update_flow_name);  


                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("1 return ");

                    return res, job_id, DES_FOLDER, PACK_NAME

                else:
                    print (LP_PATH + PACK_NAME + "\\bin\\", + " Not found")
                    return -1


            else:
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("installation failed")
                return -1

            # process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
            # output, error = process.communicate()
            # print (output)

        else:
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            print ("failed to copy")
            return -1
    else:
        print ("source package not valid")
        return -1

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("2 return ");
    return res, job_id, DES_FOLDER, PACK_NAME

def update_db(status, job_id):
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("update_db, status = ", status, " job_id = ", job_id)
    # COL_WS_NAME = "WorkStationName"
    # COL_STATUS = "JobStatus"
    #
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # query = "UPDATE `work` SET `Misc` = '8' WHERE `JobID` = 3;"
    msg = ""

    msg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   ") + "AutoQA AUTOMATIONTest return status = " + str(status)
    # query = "update " + DB_TABLE + " SET " + COL_MISC + " = concat (" + COL_MISC + ",'" + msg + "'),  " + COL_STATUS + " = " + STATUS_AUTO_QA_DONE + " where JobID = " + str(job_id)
    query = "update " + DB_TABLE + " SET " + COL_STATUS + " = '" + STATUS_AUTO_QA_DONE + "'," + COL_MISC + " = concat (" + COL_MISC + ",'\n" + msg + "') "   + " where JobID = " + str(
        job_id)

    # query = "select * from " + DB_TABLE

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("query = ", query)


    # print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "),  end=" ")
    # print ("query = " + query)
    #
    cursor.execute(query)
    cnx.commit()
    cnx.close()

def do_diff(data_string):
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("do_diff called, data_string = ", data_string)

    # now we need to be very strict with the log file path
    words = data_string.split("\\")

    print ("words = ", words, " len(words) = ", len(words))

    if len(words) != 12:
        #must be 12
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
        print ("data_string is not valid, we expect the length to be 12 after split ")
        return -1



    # golden_log = "C:\\LitePoint\\Auto_QA\\BRCM4378\\BRCM4378_Golden_Log_all.txt"
    golden_log_multi_duts = ["C:\\Li\\Auto_QA\\Automation_Related\\BRCM4378\\Log_all_golden_DUT_1.txt", "C:\\Li\\Auto_QA\\Automation_Related\\BRCM4378\\Log_all_golden_DUT_2.txt"]

    URL_ADDRESS_ARRAY = []
    for dut_id in [1,2]:     
        golden_log  = golden_log_multi_duts[dut_id-1] # 

        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")   

        print ("dut_id = ", dut_id, " golden_log = ", golden_log)
        if os.path.exists(golden_log):
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")   
            print("found golden log at: ", golden_log)

            if (data_string.endswith("\\") == False):
                data_string += "\\"
            log_need_compare = data_string + "dut_" + str(dut_id) + "\\Log\\" + "Log_all.txt"

            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            if os.path.exists(log_need_compare):
                print("found log needed to be compared at: ", log_need_compare)

                if (os.path.isfile(QA_RELATED_PATH+LOG_2_JSON_EXE)):
                    print ("generate json from log, since we found  ", QA_RELATED_PATH+LOG_2_JSON_EXE)
                    # CMD = QA_RELATED_PATH+LOG_2_JSON_EXE + " \"" + log_need_compare + "\" \"" + data_string + "dut_" + str(dut_id) + "\\Log\\\""
                    CMD = QA_RELATED_PATH+LOG_2_JSON_EXE + " \"" + log_need_compare + "\" \"" + "." + "\""

                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print("convert log to json, cmd = ", CMD)

                    res = os.system(CMD)
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("CMD res = ", res)

                    if res == 0:
                        if os.path.exists(JSON_DETAIL_FILE):
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                            print("found  ", JSON_DETAIL_FILE)
                            shutil.copyfile(r"{}".format(JSON_DETAIL_FILE), data_string + "dut_" + str(dut_id) + "\\Log\\" + JSON_DETAIL_FILE)

                        if os.path.exists(JSON_SUMMARY_FILE):
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                            shutil.copyfile(r"{}".format(JSON_SUMMARY_FILE), data_string + "dut_" + str(dut_id) + "\\Log\\" + JSON_SUMMARY_FILE)

                string_ts = words[9]

                html_file_name_only = string_ts + "_dut_" + str(dut_id) + "_diff.html"
                tmp_html = "C:\\Li\\temp\\BRCM4378\\" + html_file_name_only

                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("tmp_html = ", tmp_html)

                # delete temp html first if exists
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                if os.path.exists(tmp_html):
                    os.remove(tmp_html)
                    print("tmp_html now removed, ", tmp_html)
                else:
                    print("tmp_html does not exist, ", tmp_html)


                winmerge_cmd = 'C:\\WinMerge\\WinMergeU.exe ' + '\"' + golden_log + '\"' + ' ' + '\"' + log_need_compare + '\"' + ' -minimize -noninteractive -u -or ' + '\"' + tmp_html + '\"'

                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("2 winmerge_cmd = ", winmerge_cmd)

                res_cmd = os.system(winmerge_cmd)

                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("res_cmd = ", res_cmd)

                # sleep 60 seconds to wait for html been generated
                time.sleep(60)
                if (os.path.isfile(tmp_html) == False or os.path.getsize(tmp_html) == 0):
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("tmp html file is not valid, ", tmp_html)
                    return -1

                compare_html_full_path = "C:\\xampp\\htdocs\\AUTO_QA\\BRCM4378\\" + html_file_name_only
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("compare_html_full_path = ", compare_html_full_path)


                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                if os.path.exists(compare_html_full_path):
                    os.remove(compare_html_full_path)
                    print("The file now removed, ", compare_html_full_path)
                else:
                    print("The file does not exist, ", compare_html_full_path)

                shutil.copyfile(r"{}".format(tmp_html ),compare_html_full_path)

                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                if os.path.exists(compare_html_full_path):
                    print("The file is ready, ", compare_html_full_path)

                    URL_address = "http://iqdemo/AUTO_QA/BRCM4378/" + html_file_name_only
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("URL_address = ", URL_address)

                    URL_ADDRESS_ARRAY.append(URL_address)

                else:
                    print("The file does not exist, ", compare_html_full_path)
                    return -1



            else:
                print("log needed to be compared does not exist, ", log_need_compare)
                return -1

        else:
            print("golden log does not exist, ", golden_log)
            return -1

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("URL_ADDRESS_ARRAY = ", URL_ADDRESS_ARRAY)

    # now compare updated flow and golden flow
    if (os.path.isfile(QA_RELATED_PATH+QA_FILE_FLOW) ):
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
        print ("golden QA test flow exists, ",  QA_RELATED_PATH+QA_FILE_FLOW)

        if ( os.path.isfile( data_string+TEST_FLOW_UPDATED)):
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            print ("updated QA test flow exists, ",  data_string+TEST_FLOW_UPDATED)   

            flow_html_file_name_only = string_ts + "_flow_diff.html"
            flow_tmp_html = "C:\\Li\\temp\\BRCM4378\\" + flow_html_file_name_only

            # delete flow_tmp_html first if exists
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            if os.path.exists(flow_tmp_html):
                os.remove(flow_tmp_html)
                print("tmp_html now removed, ", flow_tmp_html)
            else:
                print("tmp_html does not exist, ", flow_tmp_html)

            winmerge_cmd = 'C:\\WinMerge\\WinMergeU.exe ' + '\"' + (QA_RELATED_PATH+QA_FILE_FLOW) + '\"' + ' ' + '\"' + (data_string+TEST_FLOW_UPDATED) + '\"' + ' -minimize -noninteractive -u -or ' + '\"' + flow_tmp_html + '\"'

            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            print ("log winmerge_cmd = ", winmerge_cmd)

            res_cmd = os.system(winmerge_cmd)

            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            print ("log winmerge_cmd res_cmd = ", res_cmd)

            # sleep 60 seconds to wait for html been generated
            time.sleep(60)
            if (os.path.isfile(flow_tmp_html) == False or os.path.getsize(flow_tmp_html) == 0):
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("flow tmp html file is not valid, ", flow_tmp_html)
                return -1

            compare_flow_html_full_path = "C:\\xampp\\htdocs\\AUTO_QA\\BRCM4378\\" + flow_html_file_name_only
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            print ("compare_log_html_full_path = ", compare_flow_html_full_path)


            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            if os.path.exists(compare_flow_html_full_path):
                os.remove(compare_flow_html_full_path)
                print("The file now removed, ", compare_flow_html_full_path)
            else:
                print("The file does not exist, ", compare_flow_html_full_path)

            shutil.copyfile(r"{}".format(flow_tmp_html ),compare_flow_html_full_path)

            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            if os.path.exists(compare_flow_html_full_path):
                print("The file is ready, ", compare_flow_html_full_path)

                URL_address_flow = "http://iqdemo/AUTO_QA/BRCM4378/" + flow_html_file_name_only
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("URL_address_log = ", URL_address_flow)

                URL_ADDRESS_ARRAY.append(URL_address_flow)

            else:
                print("The file does not exist, ", flow_compare_html_full_path)
                # return -1


        else:
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            print ("updated QA test flow NOT exists, ",  data_string+TEST_FLOW_UPDATED)    

            

    else:
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
        print ("golden QA test flow NOT exists, ",  QA_RELATED_PATH+QA_FILE_FLOW)



    

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("do_diff return URL_ADDRESS_ARRAY = ",  URL_ADDRESS_ARRAY)

    return 0,URL_ADDRESS_ARRAY

def generate_iqramp_report(data_string):
    print ("   ")
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("generate_iqramp_report data_string = ", data_string)

    # now we need to be very strict with the log file path
    words = data_string.split("\\")

    print ("words = ", words, " len(words) = ", len(words))

    if len(words) != 12:
        #must be 12
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
        print ("data_string is not valid, we expect the length to be 12 after split ")
        return -1, []

    string_ts = words[9]

    #check reportBuildr.bin
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")    
    if (os.path.isfile(IQRAMP_BUILDER_FULL_PATH)):
        print ("found IQRAMP_BUILDER_FULL_PATH,  ", IQRAMP_BUILDER_FULL_PATH)
    else:
        print ("Can not find IQRAMP_BUILDER_FULL_PATH,  ", IQRAMP_BUILDER_FULL_PATH)
        return -1, []

    #check IQRamp_template_4378.json
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")    
    if (os.path.isfile(IQRAMP_TEMPLATE_FULL_PATH)):
        print ("found IQRAMP_TEMPLATE_FULL_PATH,  ", IQRAMP_TEMPLATE_FULL_PATH)
    else:
        print ("Can not find IQRAMP_TEMPLATE_FULL_PATH,  ", IQRAMP_TEMPLATE_FULL_PATH)
        return -1, []

    #save current dir
    PATH_CURRENT = os.getcwd()
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")   
    print ("PATH_CURRENT = ", PATH_CURRENT)    

    #change current directory to QA_RELATED_PATH
    #IQRamp bug? .bin only generate pdf to same folder as .bin
    os.chdir(QA_RELATED_PATH)


    #check csv
    IQRAMP_REPORTS_URL = ["",""]
    csv_multiple_duts = ["dut_1\\Result_LP\\", "dut_2\\Result_LP\\"]
    URL_base = "http://iqdemo/AUTO_QA/BRCM4378/"
    for dut_id in [1,2]:      
        csv_full_path = data_string + csv_multiple_duts[dut_id-1] + "measurement_result.csv"
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")    
        if (os.path.isfile(csv_full_path)):
            print ("found csv_full_path,  ", csv_full_path)

            title = "IQRampReport_" + string_ts + "_dut_" + str(dut_id) + ".pdf"
            description = "\"Data Driven QA Automation for BRCM 4378 IQRamp report DUT " + str(dut_id) + "\""
            # pdf_full_path = data_string + csv_multiple_duts[dut_id-1] + title
            pdf_tmp_path = title #IQRamp bug? can only produce at same folder with .bin?
            pdf_full_path = QA_TMP_FOLDER + title

            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")   
            print ("title = ", title, " description = ", description, " pdf_full_path = ", pdf_full_path)

            CMD = IQRAMP_REPORT_BUILDER + " " + "--templates=" + IQRAMP_TEMPLATE_FULL_PATH + " --title=" + "\"" + title + "\" " + " --description=" + description + " -p \"" + pdf_tmp_path  + "\" \"" + csv_full_path + "\" "

            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")   
            print ("CMD = ", CMD)

            res = os.system(CMD)

            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            print ("CMD res = ", res)   

            #Copy generated pdf to xampp, data_string      
            IQRAMP_REPORT_HTML_PATH = "C:\\xampp\\htdocs\\AUTO_QA\\BRCM4378\\"  
            if (os.path.isfile(title)):
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")   
                    print ("Copy " + title  + " to installed bin")
                    shutil.copyfile(r"{}".format(title ),
                                    IQRAMP_REPORT_HTML_PATH + title )
 
                    if (os.path.isfile(IQRAMP_REPORT_HTML_PATH + title)):
                        IQRAMP_REPORTS_URL[dut_id-1] = (URL_base + title)

                    #copy to data_string
                    shutil.copyfile(r"{}".format(title ),
                                    data_string + title )

                    #now remove pdf from QA_RELATED_PATH
                    os.remove(title)

        else:
            print ("Can not find csv_full_path,  ", csv_full_path)
            return -1, []        


    #need change back to original directory
    os.chdir(PATH_CURRENT)

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ") 
    print ("IQRAMP_REPORTS_URL = ", IQRAMP_REPORTS_URL)

    return 0, IQRAMP_REPORTS_URL

def send_email(data_string, url_address_array, iqramp_url_array):
    print ("   ")
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("send_email data_string = ", data_string)

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("send_email url_address_array = ", url_address_array)

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("send_email iqramp_url_array = ", iqramp_url_array)

    server = smtplib.SMTP('mail2.litepoint.com', 25)



    msg = MIMEMultipart('alternative')
    msg['Subject'] = "=?utf-8?Q?=E2=9C=85=E2=9C=85=E2=9C=85?= Pass Data Driven QA BRCM4378 2 DUTs"
    msg['From'] = Sender
    msg['To'] = ", ".join(Recipients)

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    text = ""
    if (os.path.isdir(data_string)):
        print ("send_email log folder exists, ", data_string)

        # text += "Data Driven QA BRCM4378 1 DUT is done, log at <br>" + data_string + "<br><br><br><br>" + "view diff at:" + "<br>" + url_address + "<br>"
        text += "Data Driven QA BRCM4378 2 DUTs is done, log at <br>" + data_string + "<br><br><br><br>"

        if len(url_address_array) == 3:
            text += "<br><br>View diff for test flow input/return parameters at: <br>" + url_address_array[2]

        for DUT_ID in [1,2]:
            json_summary_full_path = data_string + "dut_" + str(DUT_ID) + "\\" + "Log\\" + JSON_SUMMARY_FILE
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")      
            if os.path.isfile(json_summary_full_path):
                print ("find summary json ", json_summary_full_path)
                with open(json_summary_full_path) as data_file:    
                    data = json.load(data_file)

                text += "<br><br><br><br>dut_" + str(DUT_ID) + " summary:"
                if JSON_RESULT_SUMMARY in data:
                    s = json.dumps(data[JSON_RESULT_SUMMARY], indent=4, sort_keys=True)
                    if ("fail" in s):
                        text += "<br><font color='red'>" + s + "</font>      "
                        msg['Subject'] = "=?utf-8?Q?=E2=9D=8C=E2=9D=8C=E2=9D=8C?= Fail Data Driven QA BRCM4378 2 DUTs"  
                    else:
                        text += "<br><font color='green'>" + s + "</font>      "

                if JSON_NUM_INPUTS in data:
                    s = json.dumps(data[JSON_NUM_INPUTS], indent=4, sort_keys=True)
                    text += "       Number of input parameters: " + s

                if JSON_NUM_OUTPUTS in data:
                    s = json.dumps(data[JSON_NUM_OUTPUTS], indent=4, sort_keys=True)
                    text += "       Number of return parameters: " + s + "<br>"

            else:
                print ("Can not find summary json ", json_summary_full_path)




            URL_diff_DUT_x =  url_address_array[DUT_ID-1]
            text += "<br><br>View DUT " + str(DUT_ID) +  " diff at: <br>" + URL_diff_DUT_x

            if len(iqramp_url_array[DUT_ID-1]) > 10:
                    text += "<br><br>View DUT " + str(DUT_ID) +  " IQRamp report at: <br>" + iqramp_url_array[DUT_ID-1]
        
        text += "<br><br><br><br>" + "Note: Will add limits and correlation to the IQRamp report in the new future"    
    
    else:
        print ("send_email log folder does not exists, ", data_string)
        text += "Data Drive QA BRCM4378 test is done, but log could not be found <br>"

    msg.attach(MIMEText(text, 'html'))


    server.sendmail(Sender, Recipients, msg.as_string())
    server.quit()

def remove_folder(folder):
    # check if folder exists
    if os.path.exists(LP_PATH + folder):
         # remove if exists
         shutil.rmtree(LP_PATH + folder, ignore_errors=True)
    else:
         # throw your exception to handle this special scenario
         # raise XXError("your exception")
         print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
         print ("remove_folder folder not exist, ", LP_PATH + folder )

def main():
    while True:
        num_jobs, jobs = retrieve_work_from_db()
        # print ("num_jobs = ", num_jobs)
        # print ("jobs = ", jobs)

        if num_jobs > 0:
            for row in jobs:
                # print ("row = ", row)
                # print ("len(row) = ", len(row))
                # perform one task
                res_one_task, res_job_id, res_log_path, res_package_name = perform_one_task(row)

                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("res_one_task = ", res_one_task, " res_job_id = ", res_job_id, " res_log_path = ", res_log_path)


                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("res_package_name = ", res_package_name)

                update_db(res_one_task, res_job_id)

                diff_res, diff_url_array = do_diff(res_log_path)

                iqramp_res, iqramp_url_array = generate_iqramp_report(res_log_path)

                #send out email
                send_email(res_log_path, diff_url_array, iqramp_url_array)

                #remove res_installed_full_path, only to save disk space
                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("now need remove, ", LP_PATH + res_package_name)
                remove_folder(res_package_name)


        else:
            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
            print ("retrieve_work_from_db did not find a valid task ")

        # sleep 60 seconds
        time.sleep(60)



if __name__ == "__main__":
    main()
    
    # data_string = "\\\\lphqfiler1\\Public\\Business Development\\Public\\BD_QA\\QA_Automation\\AUTO_QA_BRCM4378\\2019-06-07-15-30-10\\IQfact+_BRCM_4378_MPS_4.0.0.60\\"
    # do_diff(data_string)
    # generate_iqramp_report(data_string)

    # URL_ADDRESS_ARRAY =  ['http://iqdemo/AUTO_QA/BRCM4378/2019-01-07-17-40-03_dut_1_diff.html', 'http://iqdemo/AUTO_QA/BRCM4378/2019-01-07-17-40-03_dut_2_diff.html']
    # IQRAMP_REPORTS_URL =  ['http://iqdemo/AUTO_QA/BRCM4378/IQRampReport_2019-01-07-17-40-03_dut_1.pdf', 'http://iqdemo/AUTO_QA/BRCM4378/IQRampReport_2019-01-07-17-40-03_dut_2.pdf']   
    # send_email(data_string, URL_ADDRESS_ARRAY, IQRAMP_REPORTS_URL)

    # prepare_DUT()
    # path_bin = "C:\LitePoint\IQfact_plus\IQfact+_BRCM_4378_MPS_20190212_0645\bin\"
    # path_bin = "C:\LitePoint\IQfact_plus\IQfact+_BRCM_4378_MPS_20190212_0645"
    # update_compare_flow(path_bin)