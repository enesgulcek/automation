import os
import time

def show_old_files():
    cwd = os.getcwd()
    time_in_secs = time.time() - 30*24*60*60 # 30 gün öncesinin zamanı
    for root, dirs, files in os.walk(cwd):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_modified_time = os.path.getmtime(file_path)
            if file_modified_time < time_in_secs:
                print(f"{file_path} dosyası 30 gün öncesinden daha eski.")
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_modified_time = os.path.getmtime(dir_path)
            if dir_modified_time < time_in_secs:
                print(f"{dir_path} klasörü 30 gün öncesinden daha eski.")
