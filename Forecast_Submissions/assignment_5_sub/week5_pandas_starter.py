# Starter code for homework 5

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../data/streamflow_week5.txt'

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep = '\t', skiprows=30,
        names =['agency_cd', 'site_no', 'datetime', 'flow', 'code'])

# Expand the dates to year month day
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Sorry no more helpers past here this week, you are on your own now :)
# Hints - you will need the functions: describe, info, groupby, sort, head and tail.

# %%
# Finding the flow for this last week (9/19 - 9/25)
# Last 5 days (9/20-9/24)
data[['month', 'day', 'flow']][11584:11591]
print(data.tail())

# %%
# Question 1:
data.info() # Column names, indexes (far left column), data types (far right)

# %%
# Question 2:
data['flow'].describe()

# %%
# Question 3:
data.groupby(['month'])[['flow']].describe()

# %%
# Question 4:
data.sort_values(by='flow', ascending=False).head() # Top 5 highest
data.sort_values(by='flow', ascending=False).tail() # Bottom 5 lowest

# %%
# Question 5:
mins = np.array([])
max = np.array([])

for month in data['month']:
        add = data.sort_values(by='flow', ascending=True).head(1)
        mins.append(add)
        add2 = data.sort_values(by='flow', ascending=False).head(1)
        max.append(add2)
# %%
# Question 6:
dates = []
for day in data['datetime']:
        if (data['flow'] <= 192.15) & (data['flow'] >= 157.5):
                dates.append(day)

print(dates)
# %% 
# Experimenting

this_week = data[['month', 'day', 'flow']][11584:11591]
data[['flow']][300:330]
data['flow'][300:365].describe()
data.sort_values(by='flow', ascending=False)
data.groupby(['month', 'day'])[['flow']].mean()
# %%
