# %% 
import numpy as np
import pandas as pd

# %%
# ne marche pas
x1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x2 = np.array([1.3])

divide = x1/x2
print(divide)

for x in x1:
    if x <= divide[x-1]:
        print(x)
# %%
# from class aka this works and mine doesn't #rip
x1 = np.arange(1, 11)
x2 = 1.3

divide = x1//x2
# two slashes for integers

answer = np.max(divide)
print(answer)

# %%
# pandas
data = pd.Series([0.1, 50, 47, 1.376], index = ['a', 'b', 'c', 'd'])
data['b':'d']
print(data)
data.values
data.index
# %%
# dataframe

rng = np.random.RandomState(42)
dataframe = pd.DataFrame(rng.randint(0, 10, (3, 3)), columns=['b', 'a', 'c'], index=['row1', 'row2', 'row3'])


# %%
