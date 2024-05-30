import sys
sys.path.append('../')

from Analyze.analyze import add_geo_coordinates, get_monthly_trends, get_top_pollutants, get_pollutant_distribution_by_region, get_seasonal_trends, get_yearly_trends
from tools import get_clean_data
import matplotlib.pyplot as plt
import seaborn as sns

def plot_most_common_pollutants(data_path, top_n=10):
    """
    Plot the top N most common air pollutants from the given dataset.

    Parameters:
    data_path (str): The file path to the input CSV file containing air pollutant data.
    top_n (int): The number of top pollutants to display in the plot. Default is 10.
    """

    data = get_clean_data(data_path)
    

    most_common_pollutants = get_top_pollutants(data, top_n=top_n)

    most_common_pollutants['ShortName'] = most_common_pollutants['Name'].apply(lambda x: x[:15] + '...' if len(x) > 15 else x)
    

    labels = most_common_pollutants['ShortName'] + ' (' + most_common_pollutants['Name'] + ')'
    

    plt.figure(figsize=(10, 6))
    plt.pie(most_common_pollutants['Count'], labels=labels, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(labels))))
    plt.title(f'Top {top_n} Most Common Air Pollutants')
    plt.show()


def plot_monthly_trends(data_path):
    """
    Plot monthly average pollutant levels.

    Parameters:
    data_path (str): The file path to the input CSV file containing air pollutant data.
    """
    data = get_clean_data(data_path)
    monthly_trends = get_monthly_trends(data)

    plt.figure(figsize=(12, 8))
    plt.plot(monthly_trends['Month'], monthly_trends['Data Value'], marker='o')
    plt.title('Monthly Average Pollutant Levels')
    plt.xlabel('Month')
    plt.ylabel('Average Pollutant Level')
    plt.grid(True, linestyle='--', linewidth=0.5)
    
    plt.xticks(ticks=monthly_trends['Month'], labels=monthly_trends['Month'].dt.strftime('%Y-%m'), rotation=45)

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.show()


def plot_yearly_trends(data_path):
    """
    Plot yearly average pollutant levels.

    Parameters:
    data_path (str): The file path to the input CSV file containing air pollutant data.
    """
    data = get_clean_data(data_path)
    yearly_trends = get_yearly_trends(data)
    print(yearly_trends['Year'])


    plt.figure(figsize=(10, 6))
    plt.plot(yearly_trends['Year'], yearly_trends['Data Value'], marker='o')
    plt.title('Yearly Average Pollutant Levels')
    plt.xlabel('Year')
    plt.ylabel('Average Pollutant Level')
    plt.grid(True)
    plt.show()


def plot_seasonal_trends(data_path):
    """
    Plot seasonal average pollutant levels.

    Parameters:
    data_path (str): The file path to the input CSV file containing air pollutant data.
    """
    data = get_clean_data(data_path)
    seasonal_trends = get_seasonal_trends(data)

    plt.figure(figsize=(10, 6))
    plt.bar(seasonal_trends['Season'], seasonal_trends['Data Value'], color=['blue', 'green', 'red', 'orange'])
    plt.title('Seasonal Average Pollutant Levels')
    plt.xlabel('Season')
    plt.ylabel('Average Pollutant Level')
    plt.show()


def plot_pollutant_distribution_by_region(data_path, n=10):
    """
    Plot the distribution of pollutants across different geographical areas.

    Parameters:
    data_path (str): The file path to the input CSV file containing air pollutant data.
    n (int): The number of top regions to display.
    """
    data = get_clean_data(data_path)
    region_trends = get_pollutant_distribution_by_region(data)[:n]
    
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Data Value', y='Geo Place Name', data=region_trends, palette='viridis', hue='Geo Place Name', dodge=False, legend=False)
    plt.title('Average Pollutant Levels by Region')
    plt.xlabel('Average Pollutant Level')
    plt.ylabel('Region')
    plt.grid(True, linestyle='--', linewidth=0.5)
    
    plt.tight_layout()
    plt.show()


def plot_geographical_pollutant_heatmap(data_path, geo_coordinates):
    """
    Plot a heatmap to visualize pollutant concentrations geographically.

    Parameters:
    data_path (str): The file path to the input CSV file containing air pollutant data.
    geo_coordinates (dict): A dictionary mapping Geo Place Name to coordinates.
    """
    data = get_clean_data(data_path)
    data = add_geo_coordinates(data, geo_coordinates)

    plt.figure(figsize=(12, 8))
    heatmap_data = data.pivot_table(index='Latitude', columns='Longitude', values='Data Value', aggfunc='mean')
    sns.heatmap(heatmap_data, cmap='viridis', annot=True)
    plt.title('Geographical Heatmap of Pollutant Concentrations')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    plt.tight_layout()
    plt.show()
    
# Example usage:
# geo_coordinates = {
#     'Southeast Queens': {'lat': 40.676, 'lon': -73.756},
#     'Bensonhurst - Bay Ridge': {'lat': 40.611, 'lon': -74.011},
#     'Rockaways': {'lat': 40.586, 'lon': -73.811},
#     'Coney Island - Sheepshead Bay': {'lat': 40.583, 'lon': -73.944},
# }
