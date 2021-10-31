# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os

# %%
# Data 1, Camp Verde Stream Gage
url_1 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000&referred_module=sw&period=&begin_date=1990-01-01&end_date=2021-10-30"
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
# Plots
fig, ax = plt.subplots()
ax.plot(data1_i.index.values, data1_i['flow'], color='aqua', label='this week')
ax.set(title="This Week's Flow, 10/17 - 10/23", xlabel='Date', ylabel='Flow in CFS',
       xlim=[datetime.date(2021, 10, 24), datetime.date(2021, 10, 30)],
       ylim=[100, 175])
ax.legend(loc='lower right')
plt.setp(ax.get_xticklabels(), rotation=45)  # This rotates the x-axis labels so that they fit better on the plot
plt.show
fig.savefig("Oct24_Oct30_Flow.png")
# %%
# Generating my forecasts:

def forecasts(day_start, day_end, precip_chance):
        '''
        This function determines the week 1 and week 2 forecast predictions based on the forecasted precip in Camp Verde

        Parameters:
        "day_start" represents this past Sunday, the 24th. (int)
        "day_end" represents Saturday, the 30th. (int)
        "precip_chance" represents the forecasted amount of precipitation for Camp Verde this week. (int)

        Outputs:
        This function returns a print statement that provides the forecasted flows for week 1 and week 2. 
        '''
        week_flow1 = data1[(data1['year'] == 2021) & (data1['month'] == 10) & (data1['day'] >= day_start) & (data1['day'] <= day_end)]
        forecast_mean = np.mean(week_flow1['flow'])

        precip_to_flow = precip_chance * 14 #roughly every half inch is 14cfs
        forecast1 = forecast_mean + precip_to_flow #not used bc 0 precip
        forecast2 = forecast_mean - precip_to_flow #not used bc 0 precip

        week_min = np.min(data1_i['flow']['2021-10-24':'2021-10-30'])
        week_max = np.max(data1_i['flow']['2021-10-24':'2021-10-30'])
        difference = week_max - week_min
        forecast_wk2 = forecast_mean - difference
        prediction = print("The forecast for week 1 is:", forecast_mean, \
                "and the forecast for week 2 is:", forecast_wk2)
        return(prediction)

forecasts(24, 30, 0)
# %%
