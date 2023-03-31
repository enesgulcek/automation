import os
import datetime

folder_path = os.getcwd() # bulunduğu klasörün yolu

for file_name in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, file_name)):
        file_path = os.path.join(folder_path, file_name)
        modified_time = os.path.getmtime(file_path)
        modified_time_str = datetime.datetime.fromtimestamp(modified_time).strftime('%y%m%d-%H%M%S')
        new_file_name = '{} - {}'.format(modified_time_str, file_name)
        os.rename(file_path, os.path.join(folder_path, new_file_name))
