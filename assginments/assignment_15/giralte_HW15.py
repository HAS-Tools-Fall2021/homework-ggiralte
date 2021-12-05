# %%
import pandas as pd
import numpy as np
import datetime
import os

# %%
# Camp Verde Stream Gage
# Set the file name and path to where you have stored the data
filename = 'streamflow_week15.txt'
filepath = os.path.join(filename)
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
                     parse_dates=['datetime']
                     )

data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

data_i = data.copy()
data_i = data_i.set_index('datetime')
data_i

# %%
def forecasts(month1, month2, day_start, day_end, precip_chance):
        '''
        This function determines the week 1 and week 2 forecast predictions based on the forecasted precip in Camp Verde

        Parameters:
        "month1" represents the month of November (int)
        "month2" represents December (int)
        "day_start" represents this past Sunday, the 28th. (int)
        "day_end" represents Saturday, the 4th. (int)
        "precip_chance" represents the forecasted amount of precipitation in inches (float)

        Outputs:
        This function returns a print statement that provides the forecasted flows for week 1 and week 2. 
        '''

        week_flow = data_i['flow'][('2021-' + str(month1) + '-' + str(day_start)):('2021-' + str(month2) + '-' + str(day_end))]
        forecast_mean = np.mean(week_flow)
        print(forecast_mean)

        if precip_chance == 0:
                print("No Precip Forecasted")
                week_min = np.min(week_flow)
                week_max = np.max(week_flow)
                difference = week_max - week_min
                forecast_wk2 = week_max - difference
                prediction = print("The forecast for week 1 is:", forecast_mean, \
                        "and the forecast for week 2 is:", forecast_wk2)
        else:
                print("Precip Forecasted")
                precip_to_flow = precip_chance * 14
                forecast1 = forecast_mean + precip_to_flow
                forecast2 = forecast_mean - precip_to_flow

                prediction = print("The forecast for week 1 is:", forecast1, "cfs",
                        "and the week 2 forecast is", forecast2, "cfs")
        return(prediction)

forecasts(11, 12, 28, 4, 0.26)
# %%