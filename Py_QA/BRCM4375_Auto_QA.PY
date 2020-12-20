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


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from cgi import escape
from email.header import Header

MACHINE_ID = "AUTO_QA_BRCM4375"
STATUS_STANDBY = "STANDBY"
STATUS_INPROCESS = "IN_PROCESS"
STATUS_DONE_OK = "OK"
STATUS_DONE_ERROR = "ERROR"
STATUS_AUTO_QA_DONE = "AUTO_QA_DONE"

# copy .zip to the following folder, for local installation
QA_DOWNLOAD_PATH = "C:\\Li\Auto_QA\\downloads\\"
QA_RELATED_PATH = "C:\\Li\\Auto_QA\\Automation_Related\\"
QA_FILE_MULTI_DUT = "IQfact_MultiDUT.ini"
QA_FILE_PATHLOSS_DUT_1 = "path_loss_dut1.csv"
QA_FILE_PATHLOSS_DUT_2 = "path_loss_dut2.csv"
QA_FILE_FLOW = "4375_DataDrivenAutomation_QA.txt"

# AUTOMATION_IQVSG = "iqvsg"


COL_WS_NAME = "WorkStationName"
COL_STATUS = "JobStatus"
COL_MISC = "Misc"

config = {
    'user': 'AutoQAWorker',
    'password': 'Litepoint1',
    'host': 'iqfactsrv01',
    'database': 'autoqa',
    'raise_on_warnings': True
}

DB_TABLE = "work"

LP_PATH = "C:\\LitePoint\\IQfact_plus\\"

Sender = "DataDrivenQA_Brcm4375@litepoint.com"
Recipients = ['li.wu@litepoint.com', 'david.yin@litepoint.com', 'kaiyun.cui@litepoint.com', 'jian.sun@litepoint.com', \
                'keith.currier@litepoint.com', 'buddy.erhardt@litepoint.com', 'qing.chen@litepoint.com']
# recipients = ['li.wu@litepoint.com']

def retrieve_work_from_db():



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

                    # change dir
                    os.chdir(LP_PATH + PACK_NAME + "\\bin\\")

                    #run
                    cmd = "IQfactRun_Console.exe -multidut " + QA_FILE_MULTI_DUT + " -run " + QA_FILE_FLOW + " -exit"
                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("run cmd, ", cmd)
                    res = os.system(cmd)

                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    print ("run cmd res = ", res)

                    # # subtask
                    # for subtask in ["-QA_11AC", "-QA_11n", "-QA_11ag", "-QA_11b", "-QA_Mask", "-QA_CW", "-QA_flatness", "-QA_BT", "-zigbee"]:
                    #     print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    #     cmd = LP_PATH + PACK_NAME + "\\bin\\" + "AUTOMATIONTest.exe " + subtask + " -exit"

                    #     os.chdir(LP_PATH + PACK_NAME + "\\bin\\")

                    #     print ("run cmd, ", cmd)
                    #     res = os.system(cmd)

                    #     print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    #     print (subtask, " res = ", res)




                    # copy log file to \\lphqfiler1\Public\Business Development\Public\BD_QA\QA_Automation\AUTO_QA_AUTOMATION
                    SRC_FOLDER = LP_PATH + PACK_NAME + "\\bin\\" + "Log"
                    IGNORE_PATTERNS = ('*.iqvsa')

                    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                    if (os.path.isdir(SRC_FOLDER)):
                        print ("log folder exists, ", SRC_FOLDER)

                        DES_FOLDER = "\\\\lphqfiler1\Public\Business Development\Public\BD_QA\QA_Automation\AUTO_QA_AUTOMATION\\" + \
                                     datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + \
                                     "\\" + PACK_NAME + "\\Log";
                        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                        print ("DES_FOLDER = ", DES_FOLDER);

                        try:
                            shutil.copytree(SRC_FOLDER, DES_FOLDER, ignore=shutil.ignore_patterns(IGNORE_PATTERNS))
                            # Directories are the same
                        except shutil.Error as e:
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                            print('Directory not copied. Error: %s' % e)
                            # Any error saying that the directory doesn't exist
                        except OSError as e:
                            print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                            print('Directory not copied. Error: %s' % e)

                    else:
                        print ("log folder NOT exists, ", SRC_FOLDER)

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

    # now we need very strict with the log file path
    words = data_string.split("\\")

    print ("words = ", words, " len(words) = ", len(words))

    if len(words) != 12:
        #must be 12
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
        print ("data_string is not valid, we expect the length to be 12 after split ")
        return -1

    string_ts = words[9]
    # csv_combined_file_full_path = data_string + "//" + string_ts + ".txt"
    tmp_csv_combined_txt = "C:\\LitePoint\\IQfact_plus\\temp.txt"
    html_file_name_only = string_ts + "_diff.html"
    tmp_html = "C:\\Li\\temp\\" + html_file_name_only
    compare_html_full_path = "C:\\xampp\\htdocs\\AUTOMATION\\" + html_file_name_only
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("string_ts = ", string_ts, " tmp_csv = ", tmp_csv_combined_txt, " tmp_html = ", tmp_html)

    # delete temp files first

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    if os.path.exists(tmp_csv_combined_txt):
        os.remove(tmp_csv_combined_txt)
        print("The file now removed, ", tmp_csv_combined_txt)
    else:
        print("The file does not exist, ", tmp_csv_combined_txt)

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    if os.path.exists(tmp_html):
        os.remove(tmp_html)
        print("The file now removed, ", tmp_html)
    else:
        print("The file does not exist, ", tmp_html)

    str = os.listdir(data_string)
    for i in str:
        if i.endswith(".csv"):
            # print ("i = ", i)
            f = open(data_string + "//" + i)
            f2 = open(tmp_csv_combined_txt, "a")
            for line in f.readlines():
                small_lines = textwrap.wrap(line, 96, break_long_words=True)
                for small_line in small_lines:
                    # print ("small_line = ", small_line)
                    f2.write(small_line)
                    # if (small_line.endswith("\n") == False):
                    f2.write("\n")

            f2.close()
    # golden_log = "\\\\lphqfiler1\\Public\\Business Development\\Public\\BD_QA\\QA_Automation\\AUTO_QA_AUTOMATION\\AUTOMATION_Golden.txt"
    golden_log = "C:\\LitePoint\\IQfact_plus\\AUTOMATION_Golden.txt"

    # shutil.copyfile(r"{}".format(csv_combined_file_full_path),
    #                 tmp_csv)


    if (os.path.isfile(golden_log) == False):
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
        print ("golden_log not exist, ", golden_log)
        return -1

    if (os.path.isfile(tmp_csv_combined_txt) == False):
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
        print ("tmp_csv_combined_txt not exist, ", tmp_csv_combined_txt)
        return -1

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("golden log and compared log valid")

    diff_html_file_full_path = data_string + "//" + string_ts + "_diff.html"
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("diff_html_file_full_path = ", diff_html_file_full_path)

    winmerge_cmd = "C:\\WinMerge\\WinMergeU.exe " + golden_log + " " + tmp_csv_combined_txt + " -minimize -noninteractive -u -or " + tmp_html
    # winmerge_cmd =  "C:\\WinMerge\\WinMergeU.exe \"" + golden_log + "\" \"" + csv_combined_file_full_path + "\" -minimize -noninteractive -u -or \"" +  tmp_html + "\""
    # winmerge_cmd =  "C:\\Windows\\System32\\cmd C:\\WinMerge\\WinMergeU.exe \"" + golden_log + "\" \"" + tmp_csv_combined_txt + "\" -minimize -noninteractive -u -or \"" +  tmp_html + "\""
    # winmerge_cmd = "C:/Windows/System32/notepad.exe"
    #
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("2 winmerge_cmd = ", winmerge_cmd)

    res_cmd = os.system(winmerge_cmd)

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("res_cmd = ", res_cmd)

    if (res_cmd != 0):
        return -1

    # sleep 60 seconds to wait for html been generated
    time.sleep(60)
    if (os.path.isfile(tmp_html) == False or os.path.getsize(tmp_html) == 0):
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
        print ("tmp html file is not valid, ", tmp_html)

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
    else:
        print("The file does not exist, ", compare_html_full_path)
        return -1

    URL_address = "http://iqdemo/AUTOMATION/" + html_file_name_only
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("URL_address = ", URL_address)

    return 0,URL_address, tmp_html

def send_email(data_string, url_address, html_file_path):
    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("send_email data_string = ", data_string)

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("send_email url_address = ", url_address)

    print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    print ("send_email html_file_path = ", html_file_path)


    server = smtplib.SMTP('mail2.litepoint.com', 25)



    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Data Driven QA IQMeasure "
    msg['From'] = me
    msg['To'] = ", ".join(recipients)

    text = ""
    if (os.path.isdir(data_string)):
        print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
        print ("send_email log folder exists, ", data_string)
        text = "Data Drive QA IQMeasure test is done, log at <br>" + data_string + "<br><br><br><br>" + "view diff at:" + "<br>" + url_address + "<br>"
    else:
        text = "Data Drive QA IQMeasure test is done, but log could not be found <br>"

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
                res_one_task, res_job_id, res_log_path, res_package_name = perform_one_task(row)

                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("res_one_task = ", res_one_task, " res_job_id = ", res_job_id, " res_log_path = ", res_log_path)


                print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
                print ("res_package_name = ", res_package_name)

                update_db(res_one_task, res_job_id)

                diff_res, diff_url, diff_html_path = do_diff(res_log_path)

                #send out email
                send_email(res_log_path, diff_url, diff_html_path)

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
    # remove_folder("IQfact+_DailyBuild_VS2012_20181221_1330_r215863")
    # res_installed_full_path = "C:\\LitePoint\\IQfact_plus\\IQfact+_DailyBuild_VS2012_20181221_1330_r215863"
    # remove res_installed_full_path, only to save disk space
    # print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S   "), end=" ")
    # print ("now need remove, ", res_installed_full_path)
    # res_remove = shutil.rmtree(res_installed_full_path, ignore_errors=True)
    # print ("res_remove = ", res_remove)

    # res_log_path = "\\\\lphqfiler1\\Public\\Business Development\\Public\\BD_QA\\QA_Automation\\AUTO_QA_IQMEASURE\\2018-12-18-18-16-41\\IQfact+_DailyBuild_VS2012_20181218_0603_r215507\\Log"
    #
    # # diff_res, diff_url, diff_html_path = do_diff(res_log_path)
    # #
    # # print ("diff_res = ", diff_res)
    # # print ("diff_url = ", diff_url)
    # # print ("diff_html_path = ", diff_html_path)
    #
    # diff_url = "http://iqdemo/IQMeasure/2018-12-18-18-16-41_diff.html"
    # diff_html_path = "C:\\Li\\temp\\2018-12-18-18-16-41_diff.html"
    #
    # send_email(res_log_path, diff_url, diff_html_path)