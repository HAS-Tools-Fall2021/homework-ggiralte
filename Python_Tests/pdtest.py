# %%
import pandas as pd
import numpy as np

# %%
# Pandas Indexing Exercise 1
# start with the following dataframe of all 1's
data = np.ones((7, 3))
data_frame = pd.DataFrame(data,
                          columns=['data1', 'data2', 'data3'],
                          index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# 1. Change the values for all of the vowel rows to 3
# 2. Multiply the first 4 rows by 7
# 3. Make the dataframe into a checkerboard  of 0's and 1's using loc
# 4. Same question as 3 but without using loc
# %%
# Question 1:
data_frame.loc[['a', 'e']] = 3

# %% 
# Question 2:
data_frame.iloc[0:4, :] *= 7

# %%
# Question 3:
data_frame.loc[['a', 'e', 'c', 'g'], 1:2] = 0
data_frame.loc[['b', 'd', 'f'],0:3:2] = 0

# %%
# Quesiton 4:
data_frame.iloc[:, 0::2] = 0