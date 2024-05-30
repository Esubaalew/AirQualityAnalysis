import sys
import pandas as pd
sys.path.append('../')


from tools import get_clean_data

def get_most_common_pollutants(data, top_n=10):
    """
    Get the top N most common air pollutants from the given dataset.

    Parameters:
    data (DataFrame): The input DataFrame containing air pollutant data.
    top_n (int): The number of top pollutants to return. Default is 10.

    Returns:
    DataFrame: A DataFrame containing the top N most common air pollutants.
    """
    pollutant_counts = data.groupby('Name').size().reset_index(name='Count')
    most_common_pollutants = pollutant_counts.sort_values(by='Count', ascending=False)
    return most_common_pollutants.head(top_n)


def get_monthly_trends(data):
    """
    Calculate monthly average pollutant levels.

    Parameters:
    data (DataFrame): The input DataFrame containing air pollutant data.

    Returns:
    DataFrame: A DataFrame containing monthly average pollutant levels.
    """
    data['Month'] = data['Start_Date'].dt.to_period('M')
    monthly_trends = data.groupby('Month')['Data Value'].mean().reset_index()
    monthly_trends['Month'] = monthly_trends['Month'].dt.to_timestamp()
    return monthly_trends


