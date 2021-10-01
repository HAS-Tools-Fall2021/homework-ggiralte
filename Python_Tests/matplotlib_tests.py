# %%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
x = np.linspace(2, 10, 15)
y = np.sin(x)
plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2)
# %%
plt.scatter(x, y)

#%%
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.title('colors')
plt.colorbar();  # show color scale
# %%
