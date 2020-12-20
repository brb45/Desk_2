import os
import time
import subprocess
import shutil
import datetime
import zipfile

# install package
def install_pkg(package_loc, package_p_drive, package_name):

    # copy package first
    package_to_copy = os.path.join(package_p_drive, package_name)
    shutil.copy2(package_to_copy, package_loc)
    
    for zip_file in os.listdir(package_loc):
        zip_file = os.path.join(package_loc, zip_file)
        try:
            with zipfile.ZipFile(zip_file, "r") as file:
                file.extractall(package_loc)
                setup_exe = os.path.join(package_loc, "IQfact_plus", "setup.exe")
                while True:
                    if os.path.isfile(setup_exe):
                        break
                    else:
                        time.sleep(1)
                install_pkg = subprocess.Popen([setup_exe, "/S"])
                install_pkg.wait()

        except zipfile.BadZipFile:
            print("Error: Zipfile is corrupted.")

    #clean up zip folder
    for files in os.listdir(package_loc):
        file_to_delete = os.path.join(package_loc, files)
        if os.path.isfile(file_to_delete):
            os.remove(file_to_delete)
        else:
            shutil.rmtree(file_to_delete)

# copy test flows to bin

def copy_flows(run_dir, flow_to_test, flowfile_loc, setupfile_loc ):
    for flow_name in os.listdir(flowfile_loc):
        #flow_name = os.path.split(flow_name)[-1]
        flow_name  = flow_name.split("\\")[-1]
        src = os.path.join(flowfile_loc, flow_name)
        shutil.copy2(src, run_dir)
        flow_to_test.append(flow_name)
    for setup_file in os.listdir(setupfile_loc):
        src = os.path.join(setupfile_loc, setup_file)
        shutil.copy2(src, run_dir)

# run test flows
def run_flow(run_dir, flow_to_test, result_dir):
    os.chdir(run_dir)
    for flow_name in flow_to_test:
        # Reset DUT
        os.system("plink.exe -ssh -pw brcm1234 root@192.168.100.31 cd /root/Desktop/4378_FW/4378_18_10_336_REF; ./load_drv.sh;")
        time.sleep(40)
        # Remove old folders: Log and Result_LP before new test
        if os.path.isdir("Log"):
            shutil.rmtree("Log")
        if os.path.isdir("Result_LP"):
            shutil.rmtree("Result_LP")
        while True:
            if os.path.isdir("Log") or os.path.isdir("Result_LP"):
                time.wait(1)
            else:
                break
        run_cmd = ["IQfactRun_Console.exe", '-run', flow_name, "-repeat", "1", "-exit"]
        p = subprocess.Popen(run_cmd)
        if p.wait() != 0:
            print("RUN time error")
        test_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        test_time = "_".join(test_time.split())
        log_dir = os.path.join(result_dir, os.path.splitext(flow_name)[0], test_time)

        shutil.copytree("Log", os.path.join(log_dir, "Log"))
        shutil.copytree("Result_LP", os.path.join(log_dir, "Result_LP"))
        time.sleep(1)

def main():
    """
    *********************************************************************
    run_dir = os.getcwd()
    run_dir = r"C:\LitePoint\IQfact_plus\IQfact+_BRCM_4378_MPS_4.0.0.46\bin"

    **************************Set Up Scripts********************************
    """
    package_p_drive = r"\\lphqfiler1\Software\LitePoint\Silicon_Solutions\IQAutoBuild\projects\IQfact+_BRCM_4378_MPS"
    package_name = "IQfact+_BRCM_4378_MPS_4.0.0.50.zip"  # change as needed

    package_loc = r"C:\4378_setup\package_zip"  # package needs to be copied to package_loc
    flowfile_loc = r"C:\4378_setup\Flow"
    setupfile_loc = r"C:\4378_setup\Setup"
    run_dir = os.path.join(r"C:\LitePoint\IQfact_plus", os.path.splitext(package_name)[0], "bin")

    # Flags
    install_pkg_flg = 1
    add_flow = 1  # Copy test flows

    #**************************End Set up ***********************************

    # Install Package
    if install_pkg_flg == 1:
        install_pkg(package_loc, package_p_drive, package_name)

    # copy flow files to bin folder
    flow_to_test = []
    if add_flow == 1:
        copy_flows(run_dir, flow_to_test, flowfile_loc,  setupfile_loc)

    # Create directory to save test results
    path_list = run_dir.split("\\")[3]
    path_list = path_list.split("_")[2:]
    path_list = "_".join(path_list)
    result_dir = "_".join([path_list, "Test_Results"])  # 4378_MPS_4.0.0.46_Test_Results
    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)

    # Run Test Flows
    run_flow(run_dir, flow_to_test, result_dir)

    print("*" * 20)
    print("TEST DONE")
    print("*" * 20)
# ****************************************************************************************************


if __name__ == "__main__":
    main()



