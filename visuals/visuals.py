import sys
sys.path.append('../')

from Analyze.analyze import get_most_common_pollutants
from tools import get_clean_data
import matplotlib.pyplot as plt

def plot_most_common_pollutants(data_path, top_n=10):
    """
    Plot the top N most common air pollutants from the given dataset.

    Parameters:
    data_path (str): The file path to the input CSV file containing air pollutant data.
    top_n (int): The number of top pollutants to display in the plot. Default is 10.
    """

    data = get_clean_data(data_path)
    

    most_common_pollutants = get_most_common_pollutants(data, top_n=top_n)

    most_common_pollutants['ShortName'] = most_common_pollutants['Name'].apply(lambda x: x[:15] + '...' if len(x) > 15 else x)
    

    labels = most_common_pollutants['ShortName'] + ' (' + most_common_pollutants['Name'] + ')'
    

    plt.figure(figsize=(10, 6))
    plt.pie(most_common_pollutants['Count'], labels=labels, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(labels))))
    plt.title(f'Top {top_n} Most Common Air Pollutants')
    plt.show()

# Example usage:
# plot_most_common_pollutants('../Air_Quality.csv', top_n=10)
