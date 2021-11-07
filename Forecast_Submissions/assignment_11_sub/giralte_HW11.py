# %%
import pandas as pd
import os
import matplotlib.pyplot as plt
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import fiona
import shapely
import numpy as np
from shapely.geometry import Point
from netCDF4 import Dataset

# %%
#Import the dataset 
#NCEP Reanalysis Daily Averages, Precipitation Rate (prate)
path1 = os.path.join('../../data', "X150.135.165.51.307.9.59.3.nc")
data1 = xr.open_dataset(path1)
data1

# %%
#NCEP Reanalysis Daily Averages, Convective Precipitation Rate (cprat)
path2 = os.path.join('../../data', "X150.135.165.31.307.10.1.23.nc")
data2 = xr.open_dataset(path2)
data2

# %%
#Plot a timeseries for Precipitation Rate
lat = data1['prate']["lat"].values[0]
lon = data1['prate']["lon"].values[0]
data1_point = data1['prate'].sel(lat=lat,lon=lon) #sel = select
data1_point.shape

# use x-array to plot timeseries
data1_point.plot.line()
precip_val = data1_point.values

# Make a timeseries plot
f, ax = plt.subplots(figsize=(12, 6))
data1_point.plot.line(hue='lat',
                    marker="o",
                    ax=ax,
                    color="grey",
                    markerfacecolor="purple",
                    markeredgecolor="purple")
ax.set(title="Time Series For a Single Lat / Lon Location, Precipitation Rate")
f.savefig("Precip_Rate_Time_Series.png")

# %%
#Plot a timeseries for Convective Precipitaiton Rate
lat2 = data2['cprat']['lat'].values[0]
lon2 = data2['cprat']['lon'].values[0]
data2_point = data2['cprat'].sel(lat=lat2, lon=lon2)

data2_point.plot.line()
precip_value = data2_point.values

fig, ax = plt.subplots(figsize=(12,6))
data2_point.plot.line(hue = 'lat', marker = '*', ax=ax, color='teal', markerfacecolor='gray')
ax.set(title="Time Series For a Single Lat / Lon Location, Convective Precipitaiton Rate")
fig.savefig("Convect_Precip_Time_Series.png")
# %%
# Camp Verde Stream Gage
url_1 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000&referred_module=sw&period=&begin_date=1990-01-01&end_date=2021-11-6"
data1 = pd.read_table(url_1, skiprows=30, names=['agency_cd', 'site_no',
                                               'datetime', 'flow', 'code'],
                                               parse_dates =['datetime'])

data1['year'] = pd.DatetimeIndex(data1['datetime']).year
data1['month'] = pd.DatetimeIndex(data1['datetime']).month
data1['day'] = pd.DatetimeIndex(data1['datetime']).day
data1['dayofweek'] = pd.DatetimeIndex(data1['datetime']).dayofweek

data1_i = data1.copy()
data1_i = data1_i.set_index('datetime')
# %%
#Forecast Analysis

#data1_i['flow']['2021-11-06']

def forecasts(month1, month2, day_start, day_end):
        '''
        This function determines the week 1 and week 2 forecast predictions based on the forecasted precip in Camp Verde

        Parameters:
        "month1" represents the month of October since this week falls over a change in the months (int)
        "month2" represents November (int)
        "day_start" represents this past Sunday, the 31st. (int)
        "day_end" represents Saturday, the 6th. (int)

        Outputs:
        This function returns a print statement that provides the forecasted flows for week 1 and week 2. 
        '''
        week_flow = data1_i['flow'][('2021-' + str(month1) + '-' + str(day_start)):('2021-' + str(month2) + '-' + str(day_end))]
        #week_flow1 = data1[(data1['year'] == 2021) & (data1['month'] == month1) & (data1['day'] >= day_start) & (data1['day'] <= day_end)]
        forecast_mean = np.mean(week_flow)

        week_min = np.min(week_flow)
        week_max = np.max(week_flow)
        difference = week_max - week_min
        forecast_wk2 = week_max - difference
        prediction = print("The forecast for week 1 is:", forecast_mean, \
                "and the forecast for week 2 is:", forecast_wk2)
        return(prediction)

forecasts(10, 11, 31, 6)
# %%
