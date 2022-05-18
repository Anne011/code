import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

temp_2019 = np.linspace(-6,36,42001)
#print(temp_2019)
Corresponding_COP=0.07143*temp_2019+2.5
plt.plot(temp_2019, Corresponding_COP)
plt.ylabel("COP of ASHP") # with respect to temperature
plt.xlabel("Temperature (degree Celsius)")
plt.show()

Temperature_file_day = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/2019 air temeprature culham.csv", usecols=[9]).values
Temperature_file_wk = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/2019 air temeprature culham.csv", usecols=[5]).values
#print(Temperature_file)
Heat_Load_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/heat_loss_W_new.csv", usecols=[1]).values

COP_ASHP_2019_day = 0.07143*Temperature_file_day+2.5
COP_ASHP_2019_wk = 0.07143*Temperature_file_wk+2.5
#print(COP_ASHP_2019)

ax = plt.subplot(1,1,1)

plt.plot(COP_ASHP_2019_day[0:8761], color='royalblue')
plt.plot(COP_ASHP_2019_wk[0:8761],color='k')
#plt.plot(COP_ASHP_2019[0:53])
# plt.xticks([0,4.33,8.66,12.99,17.33,21.66,25.99,30.33,34.66,38.99,43.33,47.66,51.99])
plt.xticks([0,730,1460,2190,2920,3650,4380,5110,5840,6570,7300,8030,8760])
ax.set_xticklabels(['Jan.','Feb.','March','April','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.','Jan.'])
plt.ylabel("COP of ASHP")
plt.xlabel("Time")
plt.title('COP of ASHP in 2019')
plt.legend(['Daily COP','Weekly COP'])
plt.show()

print(max(COP_ASHP_2019_day))
print(min(COP_ASHP_2019_day))
print(sum(COP_ASHP_2019_day)/8761)

Not_absolute_power_consumption_HP = max(Heat_Load_file/(COP_ASHP_2019_day*1000))
Power_consumption_HP = max(abs(Heat_Load_file/(COP_ASHP_2019_day*1000)))

print(Not_absolute_power_consumption_HP)
print(Power_consumption_HP)

