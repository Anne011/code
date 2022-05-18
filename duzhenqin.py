import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
days=[]
for x in range(365):
    days.append(x);
y=[]
for x in range(365):
    y.append(2.71828**(-0.01108*days[x])+3.5)
plt.plot(days,y)
plt.show()


