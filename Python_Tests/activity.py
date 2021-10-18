# %%
import pandas as pd
import numpy as np
import os

# %% 
filename = 'streamflow_week5.txt'
filepath = os.path.join('../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime']
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek
# %%
# Question 1:
# avg = np.ones((1, 30))
oct_avg = np.zeros(32)
for x in range(1, 32):
    daytemp = x+1
    data_temp = data[(data['month']==10) & (data['day']==x)]
    oct_avg[x] = np.mean(data_temp['flow'])
    print("day=", daytemp, "Flow=", oct_avg[x])

# %%
# Question 2:
oct_data = data[data['month']==10]
oct_avg2 = oct_data.groupby('day').mean()['flow']
print(oct_avg2)

# %%
# Functions: 
def day_mean(month, days, data):
    avg_daily_flow = np.zeros(days)
    for x in range(days):
        data_temp = data[(data['month']==month) & (data['day']==x)]
        avg_daily_flow[x] = np.mean(data_temp['flow'])
    return avg_daily_flow

days_in_month = 31
month = 10
day_mean(month, days_in_month, data)

# %%
oct_median = np.zeros(31)
for d in range(31):
        daytemp = d+1
        tempdata = data[(data['year'] >= 2016) & (data['month'] == 10) & (data['day'] == daytemp)]
        oct_median[d] = np.median(tempdata['flow'])
        print('Iteration', d, 'Day=', daytemp, 'Flow=', oct_median[d])

# %%
# Kevin's Function:

def median_month(num_days, start_yr, month, data):
    '''
    This function allows you to determine the median flow for all of the days in a certain month in a specific year. 

    Parameters:
    "num_days" is the number of days in the month that you are choosing (int)
    "start_yr" is the year that you want to look at for the median (int)
    "month" is the month that you want to look at (int)
    "data" is the pandas dataframe file that houses all of our data

    Outputs:
    This function returns the median flows starting at "start_yr" for all of the "num_days"
    in "month"
    '''
    month_median = np.zeros(num_days)
    for d in range(num_days):
        daytemp = d+1
        tempdata = data[(data['year'] >= start_yr) & (data['month'] == month) & (data['day'] == daytemp)]
        month_median[d] = np.median(tempdata['flow'])
        description = print('Iteration', d, 'Day=', daytemp, 'Flow=', month_median[d])
    return(description)


days = 31
year = 2016
month_num = 10

median_month(days, year, month_num, data)
