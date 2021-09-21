# %%
import numpy as np
import random

# %% 
array1 = np.random.randint(1, 100, (6, 12))
print(array1)
# %%
mean = np.round(np.mean(array1), 2)
print("The mean for this array is:", mean)
std_dev = np.std(array1)
print("The standard deviation is:", std_dev)
# %%
third_col_mean = np.mean(array1[:, 2])
print("The mean for the third column is:", third_col_mean)
# %%
row_mean = np.mean(array1, axis = 1)
print(row_mean)
col_mean = np.mean(array1, axis = 0)
print(col_mean)