import re
import subprocess
import datetime
import operator
import os

maxFolders = 30
toolDir = "/home/pi/dropbox-uploader/dropbox_uploader.sh "

proc = subprocess.Popen([toolDir + "list"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

files = out.split(" ")
regex = re.compile(r"\d{2}-\w{3}-\d{2}")
dirs = {}
for file in files:
  matchObj = regex.match(file)
  if matchObj: 
    asDate = datetime.datetime.strptime(matchObj.group(), "%d-%b-%y")
    dirs[matchObj.group()] = asDate

#sort dirs by date
sortedList = sorted(dirs.items(), key=operator.itemgetter(1))

#while length of list is > threshold remove the eldest
while len(sortedList) > maxFolders:
  toRemove = sortedList.pop(0)
  removeCmd = toolDir + "delete " + toRemove[0]
  os.system(removeCmd)
