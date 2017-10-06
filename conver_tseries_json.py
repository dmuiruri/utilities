import json
import pandas as pd
import numpy as np

"""
This module is a collection of tools used to convert a dataframe into
a JSON format which allows the data to be easily parsed to around the
stack.

The structure of the data is as shown below. The account name is
picked as the column name.
    
        account_history : {
        account_name: "A name",
        history:[
            {
                date: somedate,
                balance: Euros
                },
            {
                date: somedate,
                balance: Euros
                }
            {
                date: somedate,
                balance: Euros
                }
            ]
        }

"""

def convert_dataframe_to_json(dataframe):
    """
    Convert a given dataframe into a JSON string.  A dataframe
    contains multiple accounts data and converts them all to one json
    string object. Note that the function blocks until all the objects
    are created.
    """
    json_string = {}
    json_string['account_history'] = [
        {
            'account_name': dataframe[column].name,
            'history':
                [{'date':str(date), 'account_balance':  dataframe[column][date]} for date in dataframe.index]
            } for column in dataframe.columns ]
    return json.dumps(json_string)

def convert_dataframe_to_json_gen(dataframe):
    """
    Convert a given dataframe into a JSON string.  A dataframe
    contains multiple accounts data and converts them to ine json
    string object. In this version we try to overcome the blocking
    feature and therefore implement a generator that will return an
    account at a time. An example of how to use this generator has
    been implemented in the self test.
    """
    json_string = {}
    for column in dataframe.columns:
        json_string['account_history'] = {
             'account_name': dataframe[column].name,
             'history':
                 [{'date':str(date), 'account_balance':  dataframe[column][date]} for date in dataframe.index]
             }
        yield json.dumps(json_string)

if __name__ == '__main__':
    # Simulate a dataset
    dates = pd.date_range(start='1/1/2010', end='31/12/2016', freq='M', name='Dates')
    ts_data = pd.DataFrame(np.random.rand(len(dates), 2), 
                           index=dates, columns=['Dennis', 'Bjorn']) * 1000

    # Test Function convert_dataframe_to_json_gen(dataframe)
    print("\n####### Test Function convert_dataframe_to_json_gen(dataframe) #####")
    for person in convert_dataframe_to_json_gen(ts_data):
        print(person)
    
    # Test Function: convert_dataframe_to_json(dataframe)
    print("\n####### Test Function convert_dataframe_to_json(dataframe) #####")
    print(convert_dataframe_to_json(ts_data))
