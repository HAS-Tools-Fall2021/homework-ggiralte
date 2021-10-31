# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import dataretrieval.nwis as nwis

# %%
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09402500&referred_module=sw&period=&begin_date=2000-01-01&end_date=2021-10-18"
data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                               'datetime', 'flow', 'code'],
                                               parse_dates =['datetime'])

# %%                                               
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

datai = data.copy()
datai = datai.set_index('datetime')
# %%
oct = datai[datai.index.month == 10]
datai['day'] = datai.index.day
oct_max = datai.groupby('day').max()
oct_min = datai.groupby('day').min()
oct_mean = datai.groupby('day').mean()
oct_21 = datai['2021-10-01':'2021-10-18']

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
# Different station
url2 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09429030&referred_module=sw&period=&begin_date=2000-01-01&end_date=2021-10-18"
data2 = pd.read_table(url2, skiprows=30, names=['agency_cd', 'site_no',
                                               'datetime', 'flow', 'code'],
                                               parse_dates =['datetime'])
# %%
data2['year'] = pd.DatetimeIndex(data['datetime']).year
data2['month'] = pd.DatetimeIndex(data['datetime']).month
data2['day'] = pd.DatetimeIndex(data['datetime']).day
data2['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

datai2 = data2.copy()
datai2 = datai2.set_index('datetime')
# %%
oct = datai2[datai2.index.month == 10]
datai2['day'] = datai2.index.day
oct_max = datai2.groupby('day').max()
oct_min = datai2.groupby('day').min()
oct_mean = datai2.groupby('day').mean()
oct_21 = datai2['2021-10-01':'2021-10-08']

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
station_id = "09379200"
start_date = '1989-01-01'
stop_date = '2021-10-17'
obs_day = nwis.get_record(sites=station_id, service='dv',
                          start=start_date, end=stop_date, parameterCd='00060')

# %%
oct_max2 = obs_day.groupby('day').max()
oct_min = obs_day.groupby('day').min()
oct_mean = obs_day.groupby('day').mean()
oct_21 = obs_day['2021-10-01':'2021-10-18']

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
