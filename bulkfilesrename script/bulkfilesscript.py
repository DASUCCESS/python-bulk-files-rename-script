import os

# This code rename your bulk files at ones

def script():
    i = 0
    path = "C:/Users/DASUCCESS/Pictures/test/"
    for files in os.listdir(path):
        rename_with = "nameoffile" + str(i) + ".jpg"
        folder_source =path + files
        connect_path =path + rename_with
        os.rename(folder_source, connect_path)
        i += 1
if __name__ == ' __main__ ':
    script()