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
# Make sure the file has been updated for Saturday's data
filename = 'streamflow_week7.txt'
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

# %%
# Plot 1:
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'], color='aqua', label='this week')
ax.set(title="This Week's Flow, 10/3 - 10/9", xlabel='Date', ylabel='Flow in CFS',
       xlim=[datetime.date(2021, 10, 3), datetime.date(2021, 10, 9)],
       ylim=[0, 220])
ax.legend(loc='lower right')
plt.show
fig.savefig("Oct3_Oct9_Flow.png")  # Find this file on your computer once this \
# cell has been run and insert it into the READ_ME.md file

# %%
# Plot 2:
fig, ax = plt.subplots()
for i in range(2009, 2021):
        plot_data = data[(data['year'] == i) & (data['month'] == 10)]
        ax.plot(plot_data['day'], plot_data['flow'],
                label=i)
        ax.set(title="October Flow, 10-16", xlim=[10, 16], ylim=[0, 400])
        ax.legend(loc='upper center', ncol=4)
plt.show()
fig.savefig("Oct_Trends_10_16.png")  # Find this file on your computer once this \
# cell has been run and insert it into the READ_ME.md file

# %% 
# Plot 3:
fig, ax = plt.subplots()
ax.bar(data['datetime'], data['flow'], color='aqua')
ax.set(title="Oct 17-23 Flow, 2017", xlabel='Date', ylabel='Flow in CFS',
       xlim=[datetime.date(2017, 10, 17), datetime.date(2017, 10, 23)],
       ylim=[50, 125])
ax.legend(loc='upper right')
plt.show
fig.savefig("Oct_17_23_Previous Flow.png")  # Find this file on your computer once this \
# cell has been run and insert it into the READ_ME.md file

# %%
# Week 1 (10/10-10/16) Forecast


def week_1(day_start, day_end): 
        '''
        This function determines what my forecasted flow is for 10/10-10/16 based on this past week's flow. 

        Parameters:
        "day_start" represents this past Sunday, the 3rd.
        "day_end" represents Friday, the 8th.

        Output:
        This funcion returns a print statement that provides my forecasted flow for 10/10-10/16
        based on a random number in between the maximum and minimum flow values for this current week. 
        '''
        data_range = data[(data['year'] == 2021) & (data['month'] == 10) & (data['day'] >= day_start) & (data['day'] <= day_end)]
        minimum = np.min(data_range['flow'])
        maximum = np.max(data_range['flow'])
        random.seed(9001)  # Allows for the same "random" number to be chosen
        forecast = random.randint(minimum, maximum)
        week_1_forecast = print("The forecast for 10/10-10/16 (week 1) is:", forecast, "cfs")
        return(week_1_forecast)

week_1(3, 7)  # Change this number 7 to number 8 to include up to Friday :) 

# %%
# Week 2 (10/17-10/23) Forecast


def week_2(start_yr, end_yr): 
        '''
        This function determines what my forecasted flow is for week 2 based on the max flow for Oct 17-23 over the years.

        Parameters:
        "start_yr" represents the first year of data that will be looked at
        "end_yr" represents the last year that the data will be looked at

        Output:
        This function returns a print statement that provides my forecasted flow for week 2 based
        on what the highest average flow was from October 17-23 between 2005 and 2020. 
        '''
        difference = end_yr - start_yr
        avg = np.zeros(difference)
        for i in range(start_yr, end_yr):
                years = data[(data['year'] == i) & (data['month'] == 10) & (data['day'] >= 17) & (data['day'] <= 23)]
                avg[i-start_yr] = (np.mean(years['flow']))
        max = np.amax(avg)
        week_2_forecast = print("The forecast for 10/17-10/23 (week 2) is:", max, "cfs")
        return(week_2_forecast)

week_2(2005, 2020)
# %%
