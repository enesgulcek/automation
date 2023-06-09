import os
import time

# calculate 30 days 
days = 30
time_in_secs = time.time() - (days * 24 * 60 * 60)

# current directory
folder_path = os.getcwd()

# definition to delete files and folders in a specific folder
def delete_old_files(folder_path):
    #print(folder_path)
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_modified_time = os.path.getmtime(file_path)
            #print(root)
            #print(file_name)
            #print(file_path)
            #print(file_modified_time)
            if file_modified_time < time_in_secs:
                os.remove(file_path)
                print(f"{file_path} dosyası silindi.")
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_modified_time = os.path.getmtime(dir_path)
            #print(root)
            #print(dir_name)
            #print(dir_path)
            #print(dir_modified_time)
            if dir_modified_time < time_in_secs:
                os.rmdir(dir_path)
                print(f"{dir_path} klasörü silindi.")

delete_old_files(folder_path)

