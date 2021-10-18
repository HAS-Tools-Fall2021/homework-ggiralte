# %%
# Import packages
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import random

# %%
# Set the file name and path to where you have stored the data
filename = 'streamflow_week8.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
                     parse_dates=['datetime']
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

datai = data.copy()
datai = datai.set_index('datetime')

# %%
# Plot 1:
# This plot shows what the flow has been for this current week (10/10-10/16)
fig, ax = plt.subplots()
ax.plot(datai.index.values, datai['flow'], color='aqua', label='this week')
ax.set(title="This Week's Flow, 10/10 - 10/16", xlabel='Date', ylabel='Flow in CFS',
       xlim=[datetime.date(2021, 10, 10), datetime.date(2021, 10, 16)],
       ylim=[0, 175])
ax.legend(loc='lower right')
plt.setp(ax.get_xticklabels(), rotation=45)  # This rotates the x-axis labels so that they fit better on the plot
plt.show
fig.savefig("Oct10_Oct16_Flow.png")

# %%
# Plot 2:
# This plot shows what the flow has been in the past for October 17-23
fig, ax = plt.subplots()
for i in range(2009, 2021):  # The for loop is necessary to go through a range of years
        plot_data = datai[(datai['year'] == i) & (datai['month'] == 10)]
        ax.plot(plot_data['day'], plot_data['flow'],
                label=i)
        ax.set(title="October Flow, 17-23", xlim=[17, 23], ylim=[50, 300])
        ax.legend(loc='upper center', ncol=4)  # This is the location of the legend and makes it into 4 columns
plt.show()
fig.savefig("Oct_Trends_17_23.png")

# %% 
# Plot 3:
# This plot shows the mean flow for each day from October 24-30 from 1990-2020
oct = datai[datai.index.month == 10]
datai['day'] = datai.index.day
oct_mean = datai.groupby('day').mean()  # This gets the mean for each day 

fig, ax = plt.subplots()
ax.plot(oct_mean['flow'], color='aqua')
ax.set(title="Oct 24-30 Flow Average", xlabel='Date', ylabel='Flow in CFS',
        xlim=[24,30], ylim=[200,350])
plt.show
fig.savefig("Oct_24_40_Previous Flow.png")

# %%
# Week 1 (10/17-10/23) Forecast


def week_1(day_start, day_end): 
        '''
        This function determines what my forecasted flow is for 10/17-10/23 based on the average of this past week's flow. 

        Parameters:
        "day_start" represents this past Sunday, the 10th.
        "day_end" represents Friday, the 16th.

        Output:
        This funcion returns a print statement that provides my forecasted flow for 10/17-10/23
        based on a random number in between the maximum and minimum flow values for this current week. 
        '''
        data_range = data[(data['year'] == 2021) & (data['month'] == 10) & (data['day'] >= day_start) & (data['day'] <= day_end)]
        forecast_mean = np.mean(data_range['flow'])
        week_1_forecast = print("The forecast for 10/10-10/16 (week 1) is:", forecast_mean, "cfs")
        return(week_1_forecast)

week_1(10, 16)

# %%
# Week 2 (10/24-10/30) Forecast


def week_2(month): 
        '''
        This function determines what my forecasted flow is for week 2 based on the standard deviation of the mean flow in October over the years.

        Parameters:
        "month" represents the number of the month you want, int (October = 10)

        Output:
        This function returns a print statement that provides my forecasted flow for week 2 based
        on what the highest average flow was from October 17-23 between 2005 and 2020. 
        '''
        mon = datai[datai.index.month == month]
        datai['day'] = datai.index.day
        oct_mean = datai.groupby('day').mean()
        forecast = (oct_mean['flow'][17:23].std()) + (oct_mean['flow'][24:30].std()) + (oct_mean['flow'][10:16].std())
        week_2_forecast = print("The forecast for 10/17-10/23 (week 2) is:", forecast, "cfs")
        return(week_2_forecast)

week_2(10)
# %%
