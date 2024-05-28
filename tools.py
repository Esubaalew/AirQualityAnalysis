# tools.py
'''This module contains tools that are used in whole work.'''

import pandas as pd

def get_data(file:str = "Air_Quality.csv"):
    '''This function reads the data from the csv file and returns it as a pandas dataframe.'''
    data = pd.read_csv(file)
    return data

def get_clean_data(file:str = "Air_Quality.csv"):
    '''This function reads the data from get_data function, cleans it, and returns it as a pandas dataframe.'''
    data = get_data(file)
    clean_data = data.drop(columns=['Message'])
    clean_data = clean_data.dropna(subset=['Geo Join ID', 'Geo Place Name'])
    clean_data['Start_Date'] = pd.to_datetime(clean_data['Start_Date'])

    return clean_data

