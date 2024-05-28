import sys
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