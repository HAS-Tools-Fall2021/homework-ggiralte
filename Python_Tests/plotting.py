# %%
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

data2 = pd.read_table(filepath, sep='\t', skiprows=30,
                      names =['agency_cd', 'site_no',
                              'datetime', 'flow', 'code'],
                              parse_dates =['datetime']
                      )

datai = data2.copy()
datai = datai.set_index('datetime')

# %%
oct = datai[datai.index.month == 10]
datai['day'] = datai.index.day
oct_max = datai.groupby('day').max()
oct_min = datai.groupby('day').min()
oct_mean = datai.groupby('day').mean()
oct_21 = datai['2021-10-01':'2021-10-08']

fig, ax = plt.subplots()
ax.plot(oct_max['flow'], color='orange', label='oct max')
ax.plot(oct_min['flow'], color='yellow', label='oct min')
ax.plot(oct_mean['flow'], color='blue', label='oct mean')
ax.plot(oct_21['day'], oct_21['flow'], color='green', label='2021')
ax.set(title="October", xlabel="Day of Month", ylabel='Flow',
        yscale='log')
ax.legend(loc='upper right')
plt.show

# %%
fig, ax = plt.subplots()
ax.plot(datai['flow'], color='aqua', label='this week')
ax.set(title="October", xlabel='Day of Month', ylabel='Flow in CFS')
ax.legend(loc='lower right')
plt.show

fig, ax = plt.subplots()
for i in range(1990,2021):
        plot_data = data[(data['year'] == i) & (data['month'] == 10)]
        ax.plot(plot_data['day'], plot_data['flow'],
                label=i)
        ax.set(title="October Flow, 10-16", xlim=[10, 16], ylim=[0, 400])
        ax.legend(loc='upper center', ncol=4)
# %%
