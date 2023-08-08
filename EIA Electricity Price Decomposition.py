import requests
import pandas as pd
from scipy import signal
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

def retrieve_time_series(api_key, api_url):
    # Set the API endpoint and parameters
    response = requests.get(api_url)
    data = response.json()['response']['data']
    df = pd.DataFrame(data)
    df['period'] = pd.to_datetime(df['period'], format='%Y-%m')
    df.set_index('period', inplace=True)
    df.sort_index(inplace=True)
    return df

def decompose_time_series(series):
    # Perform additive decomposition
    result = seasonal_decompose(series, model='additive')
    # Define figure and subplots
    fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1, figsize=(10,8))
    # Plot observed values
    result.observed.plot(ax=ax1, legend=False, color='dodgerblue')
    ax1.set_ylabel('Observed')
    # Plot trend values
    result.trend.plot(ax=ax2, legend=False, color='dodgerblue')
    ax2.set_ylabel('Trend')
    # Plot seasonal values
    result.seasonal.plot(ax=ax3, legend=False, color='dodgerblue')
    ax3.set_ylabel('Seasonal')
    # Plot residual values as a line
    result.resid.plot(ax=ax4, legend=False, color='dodgerblue')
    ax4.set_ylabel('Residual')
    plt.show()

# Make the API request and load the data into a DataFrame
api_key = 'API_Key_Here'
api_url = 'https://api.eia.gov/v2/electricity/retail-sales/data/?frequency=monthly&data[0]=price&facets[sectorid][]=ALL&facets[stateid][]=US&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'
api_url = f'{api_url}&api_key={api_key}'
df = retrieve_time_series(api_key, api_url) 

# Decompose the time series into its trend, seasonal, and residual components
decompose_time_series(df['price']) 
