#!/usr/bin/env python

"""
This file implements a reader that reads the various sheets of an
excel file and combining the data into one dataframe. This is assumes
that the data follows the same structure across the various sheets i.e
the column names and number of columns are the same across all sheets
to be merged. The script produces a log file(log.txt) that indicates
the sheets that have been copied.

NOTE: A potential bug in the date parsing. When the dates values are
seperated by the dot (.), joining of the dataframe does not work
well. The back slash seperator (/)seems to works fine.
"""

__author__      = "Dennis Muiruri"
__copyright__   = "03/2014"
__email__       = "denonjugush@gmail.com"


import pandas as pd
import numpy as np
import time

def read_excel_sheets(filename):

    """
    This function implements the sheet reader
    """
    data_frame = pd.DataFrame()         # DataFrame to store the data
    xls_file = pd.ExcelFile(filename)   # Handle to the excel file
    logfile = open('log.txt', 'w')      # Log file for later analysis
    sheetcounter = 0                    # Count sheets copied
    numberOfSheets = len(xls_file.sheet_names)  # No. of sheets
    nameOfSheet = xls_file.sheet_names          # List of sheet names
    logfile.write('=====> Time:  %s       <===== \n\n'  % time.asctime(time.localtime()))
    logfile.write('=====> There are %d sheets in this excel file <===== \n'  % numberOfSheets)

    # Loop through all sheets identifying those that are needed. We
    # only need daily frequency data so monthly, weekly and any other
    # miscellaneous sheets are skipped
    for i in list(range(numberOfSheets)):
        if (nameOfSheet[i].startswith('m') or
            nameOfSheet[i].startswith('w') or
            nameOfSheet[i].startswith('S')):
            pass
        else:
            logfile.write('Sheet:  %s  \n' % nameOfSheet[i])
            sheetcounter += 1
            
            frame = xls_file.parse(nameOfSheet[i], parse_dates=True, skiprows=[0,1,2, 4], index_col=0, header=0)
            if data_frame.empty:
                data_frame = frame      # cannot join empty dataframe
            else:
                # The join function is used in this case to join
                # columns (or a new data frame) horizontaly such that
                # we will end up with one large dataframe.
                data_frame=data_frame.join(frame, how='outer')          # Now we can join
    logfile.write('%d sheets copied to the data frame \n' % sheetcounter)
    logfile.close()
    return data_frame

"""
Some kind of bug/glitch has been noted. When I want to copy all the
sheets, 80 of them in this case, the data gets corrupt when we get to
sheet number 33. I.e the sheets 0-32 are all correctly added into one
data frame but when we get to number 33 the data gets corrupted, i,e
some spurious entries are noted. Weirdly though from sheet 33-80
everything proceeds as expected so the high number of colums is not
the problem. On further investigation of the code, the problem appears
to be at the join function, since if I take the sheets 0-32 into one
frame and sheets 33-80 into another frame, if I use the function join
to merge the dataframe into one data frame it gets corrupted, however
when I use the pd.concat function, the dataset is merged
correctly. The pd.concat function is done as follows \
sheet0_80=pd.concat([sheet0_32,sheet32_80])

Is this a bug or something related to multithreading in pandas and
numpy or the general python environment. But looking at the threads
utilised when python is running, there is nothing out of the ordinary
noted. i.e there are 4-6 thread on average running during this
process.

Partly, the parsing problem is solved when the dates are given such
that the seperator is the "/" character. Earlier, the seperator was
the "." character which appears to have been causing the problem.  e.g
Data in the format 2000/01/31 meaning the 31st of January the year
2000 is all joined correctly as expected. This observation should be
reported in the Python/Pandas forums.
"""
