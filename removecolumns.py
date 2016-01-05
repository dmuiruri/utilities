#!/usr/bin/env Python

"""
This module is used to remove the columns(stocks) that contain too
many null values in a given dataset. View the logfile
(logfile_removecolumns.txt) in current directory for details on
columns that get deleted. A back up of the dataframe should be created
manually prior to using this module.
"""

__author__      = "Dennis Muiruri"
__copyright__   = "03/2014"
__email__       = "denonjugush@gmail.com"

import numpy as np
import pandas as  pd
import time


def remove(dataframe, limit=250):
    """
    Remove columns with too many null values (NaN).

    dataframe: the data frame to be cleaned up

    limit: the limit for missing observations default is one year (250
    trading days)
    """
    logfile = open('logfile_removecolumns.txt', 'w')    # Create a logfile
    logfile.write('=====> Time:  %s       <=====\n'  % time.asctime(time.localtime()))
    logfile.write('=====> Log from file  %s.py  <===== \n\n'  % __name__)

    columns_overview = dataframe.columns.summary()      # Create an overview of the dataframe
    cols_list = dataframe.columns.tolist()
    cols_to_be_deleted = list()
    logfile.write('Overview of the dataframe: \n%s' % columns_overview)

    for stock in range(len(cols_list)):                 # Walk through all stocks
        if dataframe[cols_list[stock]].isnull().sum() > limit:  # Check No. of null values in a column
            cols_to_be_deleted.append(cols_list[stock])
        
    logfile.write('\nNo. of Columns with more that %d missing values:  %s\n'
                  % (limit, len(cols_to_be_deleted)))
    logfile.write('Deleted columns:\n')
    for col in cols_to_be_deleted:
        logfile.write('%s \n' % str(col))
    logfile.close()
    
    # Return updated dataframe or list of columns. See test code below
    dataframe_updated = dataframe[dataframe.columns.drop(cols_to_be_deleted)]
    return dataframe_updated
#    return cols_to_be_deleted

if __name__ == '__main__':
    df = pd.DataFrame(np.random.randn(7,5)*10)
    df.ix[2:4, 2:3] = np.nan            # Insert some nan values
    print('Original dataframe: \n %s \n' % df)

    """
    We can implement the function remove(dataframe, limit) to only
    calculate the columns to be deleted, the deletion can be handled
    in another function. This can be achived by commenting out line
    40-41 and uncommenting line 42 such that only a list containing
    names of the columns to be removed is returned to the caller. The
    code block below tests that version and creates the new data frame
    using the operation: df[df.columns.drop(cols_to_delete)]
    """
#     cols_to_delete = remove(df, limit=1)        # Cols with more than 1 null value
#     print('Cols to delete: \n %s \n' % cols_to_delete)
#     print('New dataset: \n %s\n' % df[df.columns.drop(cols_to_delete)])

    """
    This version tests the remove(datframe, limit=1) implemenation
    that returns the new dataframe with unwanted columns
    removed. Uncomment line 40-41
    """
    df_updated = remove(df, limit=1)        # Cols with more than 1 null value
    print('Updated dataframe: \n %s \n' % df_updated)
    
