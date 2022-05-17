import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

colnames=['day', 'time', 'tide']
df = pd.read_fwf(r'ASTR19_S22_group_project_data.txt', header=None, skiprows=(0,1,2), names=colnames)
x = np.linspace(1, 82, 82)
y = df['tide']
y_err = np.full(82,.25)
yfit = 2.5*-np.cos(np.pi*x)+2.48
plt.errorbar(x,y,y_err,fmt='o')
plt.plot(x, yfit)
plt.show()


