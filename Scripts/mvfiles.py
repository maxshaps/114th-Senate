import os
from sys import argv

"""
Cuts and pastes a bunch of files with names of the form <blah> _ number _ <blah>
into a subdirectory named ./number/
"""

script = argv

directory = "C:\Users\MaxShaps\Desktop\Written Documents\Python\114th Senate\Data\Raw\\"

for file in os.listdir(directory):
    src = directory + os.path.basename(file)
    dst = directory + os.path.basename(file).partition("_")[2].partition("_")[0] + "\\" + os.path.basename(file)
    os.rename(src,dst)
