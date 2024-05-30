import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sys.path.append('../')


from tools import get_clean_data

def get_top_pollutants(data, top_n=10):
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


def get_yearly_trends(data):
    """
    Calculate yearly average pollutant levels.

    Parameters:
    data (DataFrame): The input DataFrame containing air pollutant data.

    Returns:
    DataFrame: A DataFrame containing yearly average pollutant levels.
    """
    data['Year'] = data['Start_Date'].dt.year
    yearly_trends = data.groupby('Year')['Data Value'].mean().reset_index()
    return yearly_trends


def get_seasonal_trends(data):
    """
    Calculate seasonal average pollutant levels.

    Parameters:
    data (DataFrame): The input DataFrame containing air pollutant data.

    Returns:
    DataFrame: A DataFrame containing seasonal average pollutant levels.
    """
    data['Month'] = data['Start_Date'].dt.month
    data['Season'] = data['Month'].apply(lambda x: (x%12 + 3)//3)
    season_labels = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
    data['Season'] = data['Season'].map(season_labels)
    seasonal_trends = data.groupby('Season')['Data Value'].mean().reset_index()
    return seasonal_trends


def get_pollutant_distribution_by_region(data):
    """
    Calculate the average pollutant levels for each region.

    Parameters:
    data (DataFrame): The input DataFrame containing air pollutant data.

    Returns:
    DataFrame: A DataFrame with columns 'Geo Place Name' and 'Data Value' for average pollutant levels.
    """
    region_trends = data.groupby('Geo Place Name')['Data Value'].mean().reset_index()
    region_trends = region_trends.sort_values(by='Data Value', ascending=False)
    return region_trends

def add_geo_coordinates(data, geo_coordinates):
    """
    Add geographical coordinates to the dataset based on Geo Place Name.

    Parameters:
    data (DataFrame): The input DataFrame containing air pollutant data.
    geo_coordinates (dict): A dictionary mapping Geo Place Name to coordinates.

    Returns:
    DataFrame: DataFrame with latitude and longitude columns added.
    """
    data['Latitude'] = data['Geo Place Name'].map(lambda x: geo_coordinates.get(x, {}).get('lat', None))
    data['Longitude'] = data['Geo Place Name'].map(lambda x: geo_coordinates.get(x, {}).get('lon', None))
    return data.dropna(subset=['Latitude', 'Longitude'])


def identify_high_pollution_events(data, threshold):
    """
    Identify high pollution events based on a threshold value.

    Parameters:
    data (DataFrame): The input DataFrame containing air pollutant data.
    threshold (float): The threshold value for high pollution events.

    Returns:
    DataFrame: A DataFrame containing high pollution events.
    """
    high_pollution_events = data[data['Data Value'] > threshold]
    return high_pollution_events

def assess_policy_impacts(before_data, after_data):
    """
    Assess the impacts of policies on pollutant levels.

    Parameters:
    before_data (DataFrame): DataFrame containing air pollutant data before policy implementation.
    after_data (DataFrame): DataFrame containing air pollutant data after policy implementation.

    Returns:
    DataFrame: A DataFrame containing the changes in pollutant levels after policy implementation.
    """
    before_mean = before_data['Data Value'].mean()
    after_mean = after_data['Data Value'].mean()
    impact = after_mean - before_mean
    return impact


def calculate_summary_statistics(data):
    """
    Calculate summary statistics for pollutant levels.

    Parameters:
    data (DataFrame): The input DataFrame containing air pollutant data.

    Returns:
    dict: A dictionary containing summary statistics (mean, median, std, min, max).
    """
    summary_stats = {
        'Mean': data['Data Value'].mean(),
        'Median': data['Data Value'].median(),
        'Standard Deviation': data['Data Value'].std(),
        'Minimum': data['Data Value'].min(),
        'Maximum': data['Data Value'].max()
    }
    return summary_stats

def analyze_distribution(data):
    """
    Analyze the distribution of pollutant levels.

    Parameters:
    data (DataFrame): The input DataFrame containing air pollutant data.
    """
    plt.figure(figsize=(12, 6))
    sns.histplot(data['Data Value'], kde=True, bins=20, color='skyblue')
    plt.title('Distribution of Pollutant Levels')
    plt.xlabel('Pollutant Level')
    plt.ylabel('Frequency')
    plt.grid(True, linestyle='--', linewidth=0.5)

    plt.figure(figsize=(10, 6))
    sns.boxplot(data['Data Value'], color='lightgreen')
    plt.title('Box Plot of Pollutant Levels')
    plt.xlabel('Pollutant Level')

    plt.tight_layout()
    plt.show()


# Example usage
data = get_clean_data('../Air_Quality.csv')
analyze_distribution(data)