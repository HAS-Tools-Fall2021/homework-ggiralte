# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json 
import urllib.request as req
import urllib
from sklearn.linear_model import LinearRegression
import datetime

# %%
# Data 1, Camp Verde Stream Gage
url_1 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000&referred_module=sw&period=&begin_date=1990-01-01&end_date=2021-10-23"
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
# Camp Verde Streamflow Plot 1:
fig, ax = plt.subplots()
ax.plot(data1_i.index.values, data1_i['flow'], color='aqua', label='this week')
ax.set(title="This Week's Flow, 10/17 - 10/23", xlabel='Date', ylabel='Flow in CFS',
       xlim=[datetime.date(2021, 10, 17), datetime.date(2021, 10, 23)],
       ylim=[100, 175])
ax.legend(loc='lower right')
plt.setp(ax.get_xticklabels(), rotation=45)  # This rotates the x-axis labels so that they fit better on the plot
plt.show
fig.savefig("Oct17_Oct23_Flow.png")

# %%
# Camp Verde Streamflow Plot 2:
oct = data1_i[data1_i.index.month == 10]
data1_i['day'] = data1_i.index.day
oct_mean = data1_i.groupby('day').mean()  # This gets the mean for each day 
oct_min = data1_i.groupby('day').min()
oct_max = data1_i.groupby('day').max()

fig, ax = plt.subplots()
ax.plot(oct_mean['flow'], color='aqua', label='oct mean')
ax.plot(oct_min['flow'], color='green', label='oct min')
ax.plot(oct_max['flow'], color='red', label='oct max')
ax.set(title="Oct 24-30 Flow Mean, Max, and Min", xlabel='Date', ylabel='Flow in CFS',
        xlim=[24,30], yscale='log')
ax.legend(loc='upper left')
plt.show
fig.savefig("Oct_24_30_Previous Flow.png")

# %%
# Camp Verde Streamflow Plot 3:
fig, ax = plt.subplots()
for i in range(2009, 2021):  # The for loop is necessary to go through a range of years
        plot_data = data1_i[(data1_i['year'] == i) & (data1_i['month'] == 10)]
        ax.plot(plot_data['day'], plot_data['flow'],
                label=i)
        ax.set(title="October Flow, 24-30", xlim=[24, 30], ylim=[50, 300])
        ax.legend(loc='upper center', ncol=4)  # This is the location of the legend and makes it into 4 columns
plt.show()
fig.savefig("Oct_Trends_24_30.png")

# %%
# Point on Daymet east of Cottonwood
# I chose this plot because it's close to where the Verde River starts so if they get
# precipitation, it's likely that the streamflow could increase. 
url = "https://daymet.ornl.gov/single-pixel/api/data?lat=34.7525&lon=-111.9058&vars=dayl,prcp,srad,swe,tmax,tmin,vp&start=1990-01-01&end=2020-12-31&format=json"
response = req.urlopen(url)
responseDict = json.loads(response.read())
responseDict['data'].keys()
year = responseDict['data']['year']
yearday = responseDict['data']['yday']
precip = responseDict['data']['prcp (mm/day)']

#make a dataframe from the data
data = pd.DataFrame({'year': year,
                     'yearday': yearday, "precip": precip})

# %%
# Daymet Plot 1:
fig, ax = plt.subplots()
ax.bar(data['year'], data['precip'], width=0.5, color='green')
ax.set(title="Precip East of Cottonwood", yscale='log')
plt.show
fig.savefig("Cottonwood_Precip.png")

# %%
# Daymet Plot 2:
#data = pd.DataFrame(datetime.datetime(year, 1, 1) + datetime.timedelta(yearday - 1))

fig, ax = plt.subplots()
ax.bar(data["year"][2020.0], data['precip'], width=0.2, color='green')
ax.set(title="2020 Precip", xlabel="Yearday", ylabel="Precip",
        xlim=[0, 365], ylim=[0, 10])
plt.setp(ax.get_xticklabels(), rotation=45) 
plt.show
fig.savefig("Cottonwood20_Precip.png")
# I truly do not know why this plot is blank

# %% 
# Linear Regression:
flow_weekly = data1.resample("W", on='datetime').mean()
flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)

train = flow_weekly[2:800][['flow', 'flow_tm1', 'flow_tm2']]
test = flow_weekly[800:][['flow', 'flow_tm1', 'flow_tm2']]

model2 = LinearRegression()
x2 = train[['flow_tm1', 'flow_tm2']]
y = train['flow'].values
model2.fit(x2, y)
r_sq = model2.score(x2, y)
print('coefficient of determination:', np.round(r_sq, 2))
print('intercept:', np.round(model2.intercept_, 2))
print('slope:', np.round(model2.coef_, 2))

q_pred2_train = model2.predict(train[['flow_tm1', 'flow_tm2']])

# %%
# Linear Regression Plot:
fig, ax = plt.subplots()
ax.plot(train['flow'], color='grey', linewidth=2, label='observed')
ax.plot(train.index, q_pred2_train, color='blue', linestyle='--',
        label='simulated 2 lag')
ax.set(title="Observed Flow", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log')
ax.legend()
fig.savefig("Linear_Regression.png")

# %%
# Generating my forecasts:

def forecasts(day_start, day_end, precip_chance):
        '''
        This function determines the week 1 and week 2 forecast predictions based on the forecasted precip in Camp Verde

        Parameters:
        "day_start" represents this past Sunday, the 17th. (int)
        "day_end" represents Friday, the 23rd. (int)
        "precip_chance" represents the forecasted amount of precipitation for Camp Verde this week. (int)

        Outputs:
        This function returns a print statement that provides the forecasted flows for week 1 and week 2. 
        '''
        week_flow1 = data1[(data1['year'] == 2021) & (data1['month'] == 10) & (data1['day'] >= day_start) & (data1['day'] <= day_end)]
        forecast_mean = np.mean(week_flow1['flow'])
        precip_to_flow = precip_chance * 14 #roughly every half inch is 14cfs
        forecast1 = forecast_mean + precip_to_flow
        forecast2 = forecast_mean - precip_to_flow
        prediction = print("The forecast for week 1 is:", forecast1, \
                "And the forecast for week 2 is:", forecast2)
        return(prediction)

forecasts(17, 23, 0.2)
# %%
