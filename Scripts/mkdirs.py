import os
from sys import argv

"""
Creates a bunch of numbered directories spanning the numerical range
firstDirNum to lastDirNum
"""

script, firstDirNum, lastDirNum = argv

directory = "C:\Users\MaxShaps\Desktop\Written Documents\Python\114th Senate\Data\Raw\\" + firstDirNum

dirNum = int(firstDirNum)

while dirNum <= int(lastDirNum):
    if not os.path.exists(directory):
        os.makedirs(directory)
    dirNum += 1
    directory = "C:\Users\MaxShaps\Desktop\Written Documents\Python\114th Senate\Data\Raw\\" + str(dirNum)
