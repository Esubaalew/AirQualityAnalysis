#tools.py
'''This module contains tools that are used in whole work.'''

import pandas as pd

def get_data():
    '''This function reads the data from the csv file and returns it as a pandas dataframe.'''

    data = pd.read_csv("Air_Quality.csv")
    return data