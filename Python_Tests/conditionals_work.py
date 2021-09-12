# %%

import os
import numpy as np
import earthpy as et

avg_month_precip_url = "https://ndownloader.figshare.com/files/12565616"
et.data.get_data(url=avg_month_precip_url)

os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))

avg_month_precip_path = os.path.join("data", "earthpy-downloads", "avg-monthly-precip.txt")

# %%
if os.path.exists(avg_month_precip_path):
    print("This is a valid path.")
    avg_month_precip = np.loadtxt(avg_month_precip_path)
    print(avg_month_precip)
else:
    print("This path does not exist. :(")

# %%
