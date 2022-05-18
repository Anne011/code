# COP wrt time of the whole system
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.optimize import fsolve
#Heat_Loss_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/heat_loss_W_new.csv", usecols=[1]).values
Heat_Load_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/five years.csv", usecols=[0]).values
#Outlet_Temp_BTES_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/BTESTemperatures.csv", usecols=[1]).values
Outlet_Temp_BTES_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/6666years.csv", usecols=[1]).values
#COP_file_wk = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/heat_load_J_new.csv", usecols=[9]).values


Cp = 4200 #Jouls/(kg*degree)
T_supply = 70 #degree
T_return = 50 #degree
second_in_day = 24*3600 #s
m_BTES = 3.7 #kg/s !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
eta = 0.42 #fraction of Carnot Cycle
#T_BTES = 42.6 #degree
T_BTES = Outlet_Temp_BTES_file
#print(T_BTES)

#mass flow rate in HP
ax = plt.subplot(1,1,1)
#m_HP = Heat_Loss_file[0:8761]/(Cp*(T_supply - T_return))
m_HP = Heat_Load_file[0:365*7]/3600/24/(Cp*(T_supply - T_return))
m_HP_peak_cooling = max(m_HP)
m_HP_peak_heating = max(abs(m_HP))

#plt.plot(abs(m_HP[0:8761]))
plt.plot(abs(m_HP[0:365*7]))
#plt.xticks([0,730,1460,2190,2920,3650,4380,5110,5840,6570,7300,8030,8760])
plt.xticks([0,365,365*2,365*3,365*4,365*5,365*6,365*7])
ax.set_xticklabels(['Year 1','Year 2','Year 3','Year 4','Year 5','Year 6','Year 7','Year 8'])
plt.ylabel("Mass flow rate in Building (kg/s)")
plt.xlabel("Year")
plt.title('Mass Flow Rate of Water in the Building in 2019')
plt.show()

print(m_HP_peak_cooling)
print(m_HP_peak_heating)
#print(list)

d = {'mass_flow_rate': np.array(m_HP[:,0])}
df = pd.DataFrame(data=d)
df.to_csv("m_new_5.csv")

#COP
m_HP_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/m_new_5.csv", usecols=[1]).values
#print(m_HP_file)
ax = plt.subplot(1,1,1)
#star = m_HP_file[0:365]*(T_supply-T_return)
#COP = (m_HP_file[0:8761]*(T_supply-T_return)+(m_BTES*(T_supply+273)*eta))/(abs(m_HP_file[0:8761])*(T_supply-T_return)-m_BTES*(T_BTES-T_supply))
#COP = (m_HP_file[0:365*5]*(T_supply-T_return)+(m_BTES*(T_supply+273)*eta))/(abs(m_HP_file[0:365*5])*(T_supply-T_return)-m_BTES*(40-T_supply))
COP = (m_HP_file[0:365*7]*(T_supply-T_return)+(m_BTES*(T_supply+273)*eta))/(abs(m_HP_file[0:365*7])*(T_supply-T_return)-m_BTES*(T_BTES-T_supply))

#plt.plot(COP[0:8761])
plt.plot(COP[0:365*7],color = 'royalblue')
#plt.plot(COP_file_wk[0:365],color = 'k')
#plt.xticks([0,730,1460,2190,2920,3650,4380,5110,5840,6570,7300,8030,8760])
plt.xticks([0,365,365*2,365*3,365*4,365*5,365*6,365*7])
ax.set_xticklabels(['Year 1','Year 2','Year 3','Year 4','Year 5','Year 6','Year 7','Year 8'])
plt.xlabel("Time")
plt.ylabel("COP of the System")
#plt.title('Coefficient of Performance (COP) of the System in 5 Years')
plt.legend(['Daily COP'])
#plt.legend(['Daily COP','Weekly COP'])
plt.show()
#print(m_HP_file[0:365]*(T_supply-T_return)+(m_BTES*(T_supply)*eta))
#print((m_HP_file[0:365]*(T_supply-T_return)-m_BTES*(T_BTES)+m_BTES*(T_supply)))

#print(Heat_Load_file)
Peak_COP = max(COP)
Lowest_COP = min(COP)

print(Peak_COP)
print(Lowest_COP)
#print(COP)


#Power consumption
Not_absolute_power_consumption_HP = Heat_Load_file/(COP*1000)/24/3600
Power_consumption_HP = abs(Heat_Load_file/(COP*1000)/24/3600)

ax = plt.subplot(1,1,1)
#plt.plot(Power_consumption_HP[0:8761])
plt.plot(Power_consumption_HP[0:365*7])
#plt.xticks([0,730,1460,2190,2920,3650,4380,5110,5840,6570,7300,8030,8760])
plt.xticks([0,365,365*2,365*3,365*4,365*5,365*6,365*7])
ax.set_xticklabels(['Year 1','Year 2','Year 3','Year 4','Year 5','Year 6','Year 7','Year 8'])
plt.ylabel("Power Consumption (kW)")
plt.xlabel("Time")
plt.title('Power Consumption of Heat Pump in 2019')
plt.show()

peak_power_consumption_HP = max(Power_consumption_HP)
peak_power_consumption_HP_cooling = max(Not_absolute_power_consumption_HP)
print(peak_power_consumption_HP)
print(peak_power_consumption_HP_cooling)


#Reinjection Temperature
T_reinjection = T_supply - (eta*(T_supply+273.15)/COP[0:365*5])
#print(T_reinjection)

#c = {'mass_flow_rate': np.array(abs(m_HP[:,0])),'COP_heat_demand': np.array(abs(COP[:,0])),'Power Consumption':np.array(abs(Power_consumption_HP[:,0])),'T_Reinjection':np.array(abs(T_reinjection[:,0]))}
#dfc = pd.DataFrame(data=c)
#dfc.to_csv("COPheatdemand.csv")