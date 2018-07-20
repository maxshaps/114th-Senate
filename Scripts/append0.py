import os
from sys import argv


"""
Appends the string " (0)" to appropriate files in various directories
"""

script, firstSubDir, lastSubDir = argv

directory = "C:\Users\MaxShaps\Desktop\Written Documents\Python\114th Senate\Data\Raw\\"

currentSubDir = firstSubDir

while int(currentSubDir) <= int(lastSubDir):
    for file in os.listdir(directory + currentSubDir):
        if "(" not in os.path.basename(file):
            oldName = os.path.basename(file)
            newName = oldName.partition(".")[0] + " (0)." + oldName.partition(".")[2]
            location = directory + currentSubDir + "\\"
            os.rename(location + oldName, location + newName)
    currentSubDir = str(int(currentSubDir) + 1)
