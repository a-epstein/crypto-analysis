#%% [markdown]

# Bitcoin Analysis
# 1. What time of day do highs and lows of the day occur?
# 2. What days of the week have the highest highs, and the lowest lows?

#%%
# Import libraries
import requests
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline


# %%
# Access Cryptowatch api and retrieve data summary
kraken_url = 'https://api.cryptowat.ch/markets/kraken/btcusd/summary'
resp = requests.get(kraken_url)
resp.json()

# %%
# Get historic data from OHLC (open high low close)
kraken_data = 'https://api.cryptowat.ch/markets/kraken/btcusd/ohlc'
resp = requests.get(kraken_data)
doc = resp.json()

# %% [markdown]
# Each value is a list that contains:

# Timestamp (expressed as unix epoch)
# Open Price
# High Price
# Low Price
# Close Price
# Volume
# Not used


# %%
# List of periods
periods = {
    '60': '1m',  # 1 Minute
    '180': '3m', # 3 Minutes
    '300': '5m',
    '900': '15m',
    '1800': '30m',
    '3600': '1h', # 1 Hour
    '7200': '2h',
    '14400': '4h',
    '21600': '6h',
    '43200': '12h',
    '86400': '1d', # 1 Day
    '259200': '3d',
    '604800': '1w', # 1 Week
}

# %%
# Looking at 1 week periods
week = '604800'
params = {'periods': week}
resp = requests.get(kraken_data, params)
resp.ok

# %%
data = resp.json() # convert json to python data

# %%
df = pd.DataFrame(data['result'][periods], columns=['CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume', 'NA'])
df.head()

# %%
