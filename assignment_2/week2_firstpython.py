# %%
# Step 1 - Download the data from the USGS website
# https: // waterdata.usgs.gov/nwis/dv?referred_module = sw & site_no = 09506000
# For now you should save this file to the directory you put this script in

# %%
# Step 2 - Import the modules we will use
import pandas as pd
import matplotlib.pyplot as plt
import os

# %% 
# Step 3 - Read in the file in as dataframe
# You will need to change the filename to match what you downloaded
filename = 'streamflow_week2.txt'
filepath = os.path.join('../data', filename)

data=pd.read_table(filepath, sep = '\t', skiprows=30, 
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )
data = data.set_index('datetime')


# %%
# Step 4 - Look at the data
print(data.shape)  # See how many rows and columns the data has
data.head(6) # look at the first x rows of the data
data.tail(6) # look at the last  x rows  of the data

data.iloc[350:360] # grab any subset of rows to look at
data.flow[11550:11580]  #Grab a subset of just the flow data dat look at
data.loc['2018-09-02':'2018-09-20']  #find a specific date
data.flow['2021-08-19':'2021-08-31'] 

# %%
# Step 5 - Make a plot of the data
# Change the numbers on the followin lines to plot a different portion of the data
ax=data.iloc[400:500]['flow'].plot(linewidth=0.5)
ax.set_ylabel('Daily Flow [cfs]')
ax.set_xlabel('Date')

