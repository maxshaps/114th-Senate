import os
from sys import argv

"""
Concatenates a series of csv files in a base directory and saves the concatenation
into an output directory.  Since all files contain a header line, only the header
from the first file is retained.
"""


script = argv

baseDirectory = "C:\Users\MaxShaps\Desktop\Written Documents\Python\114th Senate\Data\Raw\Preprocessed\\"
outputDirectory = "C:\Users\MaxShaps\Desktop\Written Documents\Python\114th Senate\Data\\"
outputFileName = "114th Senate Roll Call Votes.csv"
header_saved = False

with open(outputDirectory + outputFileName, 'w') as out_file:
    for r, d, f in os.walk(baseDirectory):
        for file in f:
            with open(os.path.join(r, file)) as current_file:
                header = next(current_file)
                if not header_saved:
                    out_file.write(header)
                    header_saved = True
                for line in current_file:
                    out_file.write(line)
