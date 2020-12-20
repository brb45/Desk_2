import os
import time

def get_file_size(file_path_server):
    if os.path.isfile(file_path_server):
        st = os.stat(file_path_server)
        return st.file_size
    else:
        return -1

def is_file_exist(file_path_server,file_path, time_to_wait):
    time_cnter = 0
    while not os.path.exists(file_path):
        time.sleep(1)
        time_cnter+=1
        if time_cnter > time_to_wait:
            print(f"{file_path} does not exist")
            return False
    if os.path.isfile(file_path):
        file_size = get_file_size(file_path_server)
        cnt = 0
        while True:
            download_size = get_file_size(file_path)
            if download_size != file_size:
                time.sleep(1)
                cnt += 1
            else:
                break
            if cnt > 10:
                break
        return download_size == file_size
    else:
        raise ValueError(f"{file_path} doesn't exist")

def download_wait(path_to_downloads):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 20:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(path_to_downloads):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds
