import os
import datetime

path="/home/pi/cam/"
timeNow = datetime.datetime.now().strftime('%d%m%y-%H%M%S')
transferPath = "/home/pi/" + timeNow + "/"

def upload_files():
    today = datetime.datetime.today().strftime('%d-%b-%y')
    os.chdir(transferPath)
    for files in os.listdir("."):
        if files.endswith(".jpg"):
            cmd = "/home/pi/dropbox-uploader/dropbox_uploader.sh upload " + transferPath + files + " ./" + today + "/"
            os.system(cmd)

def transfer_files():
    if not os.path.exists(path):
        return
    os.chdir(path)
    if not os.path.exists(transferPath):
        os.system("sudo mkdir " + transferPath)
    cmd = "sudo mv " + path + "*.jpg " + transferPath
    os.system(cmd)

def remove_files():
    os.system("sudo rm -rf " + transferPath)

transfer_files()
upload_files()
remove_files()

