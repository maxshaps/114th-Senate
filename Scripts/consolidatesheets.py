import os
from sys import argv
import pandas as pd

"""
Finds a bunch of multisheet xls files in a directory, extracts the important information
to a single pandas dataframe, and exports the dataframe to an appropriately named
csv file in an appropriate directory
"""

script = argv

rawDirectory = "C:\Users\MaxShaps\Desktop\Written Documents\Python\114th Senate\Data\Raw\\"
preprocessedDirectory = "C:\Users\MaxShaps\Desktop\Written Documents\Python\114th Senate\Data\Raw\Preprocessed\\"

for r, d, f in os.walk(rawDirectory):
    for file in f:
        if file.endswith(".xls"):
            df1 = pd.read_excel(os.path.join(r, file), sheet_name=0)
            df2 = pd.read_excel(os.path.join(r, file), sheet_name=1)
            df3 = pd.read_excel(os.path.join(r, file), sheet_name=2)


            dfout = pd.merge(df1, df2, on=['icpsr','id','name','state_abbrev'], how='inner')
            dfout = dfout.drop(columns=['district_code','cqlabel'])

            df3 = df3.drop(columns=['vote'])
            df3 = df3.rename(index=str, columns={'id': 'rollcallvote_id'})

            df3 = pd.concat([df3]*len(dfout), ignore_index=True)

            dfout = dfout.join(df3)
            outfilename = preprocessedDirectory + str(dfout['rollnumber'][0]) + '.csv'
            dfout.to_csv(path_or_buf=outfilename, header=True)
