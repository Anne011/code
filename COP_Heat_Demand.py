# COP wrt time of the whole system
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.optimize import fsolve
Heat_Loss_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/heat_loss_W_new.csv", usecols=[1]).values
Heat_Load_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/heat_load_J_new.csv", usecols=[1]).values
#Outlet_Temp_BTES_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/BTESTemperatures.csv", usecols=[1]).values
#Outlet_Temp_BTES_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/heat_load_J_new.csv", usecols=[10]).values
Outlet_Temp_BTES_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/TBTESAfterFinal.csv", usecols=[1]).values
COP_file_wk = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/heat_load_J_new.csv", usecols=[19]).values
#Outlet_Temp_BTES_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/inlet_temp_BTES_with_4.2heat_in.csv", usecols=[1]).values


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
m_HP = Heat_Load_file[0:365]/3600/24/(Cp*(T_supply - T_return))
m_HP_peak_cooling = max(m_HP)
m_HP_peak_heating = max(abs(m_HP))

#plt.plot(abs(m_HP[0:8761]))
plt.plot(abs(m_HP[0:365]))
#plt.xticks([0,730,1460,2190,2920,3650,4380,5110,5840,6570,7300,8030,8760])
plt.xticks([0,31,59,90,120,151,181,212,243,273,304,334,365])
ax.set_xticklabels(['Jan.','Feb.','March','April','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.','Jan.'])
plt.ylabel("Mass flow rate in Building (kg/s)")
plt.xlabel("Time")
plt.title('Mass Flow Rate of Water in the Building in 2019')
plt.show()

print(m_HP_peak_cooling)
print(m_HP_peak_heating)
#print(list)

d = {'mass_flow_rate': np.array(m_HP[:,0])}
df = pd.DataFrame(data=d)
df.to_csv("m_new.csv")

#COP
m_HP_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/m_new.csv", usecols=[1]).values
#print(m_HP_file)
ax = plt.subplot(1,1,1)
#star = m_HP_file[0:365]*(T_supply-T_return)
#COP = (m_HP_file[0:8761]*(T_supply-T_return)+(m_BTES*(T_supply+273)*eta))/(abs(m_HP_file[0:8761])*(T_supply-T_return)-m_BTES*(T_BTES-T_supply))
#COP = (abs(m_HP_file[0:365])*(T_supply-T_return)+(m_BTES*(T_supply+273)*eta))/(abs(m_HP_file[0:365])*(T_supply-T_return)-m_BTES*(30-T_supply))
COP = (abs(m_HP_file[0:365])*(T_supply-T_return)+(m_BTES*(T_supply+273)*eta))/(abs(m_HP_file[0:365])*(T_supply-T_return)-m_BTES*(T_BTES-T_supply))

days=[]
for x in range(396):
    days.append(x);
y=[]
for x in range(396):
    y.append(2.71828**(-0.009*days[x])+3.496)

a = np.zeros(shape = (396,1))
a[:,0] = 3.496

#plt.plot(COP[0:8761])
plt.plot(COP[0:365],color = 'royalblue')
#plt.plot(COP_file_wk[0:365],color = 'k')
#plt.plot(days,y,color = 'tomato')
#plt.plot(days,a,'k--')
#plt.xticks([0,730,1460,2190,2920,3650,4380,5110,5840,6570,7300,8030,8760])
plt.xticks([0,31,59,90,120,151,181,212,243,273,304,334,365])
ax.set_xticklabels(['Jan.','Feb.','March','April','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.','Jan.'])
#plt.yticks([2.5,3.0,3.5,4.0,4.5])
plt.xlabel("Time")
plt.ylabel("COP of the System")
#plt.title('Coefficient of Performance (COP) of the System in 2019')
#plt.legend(['Daily COP','COP asymptote','future average COP = 3.5'])
#plt.legend(['Daily COP'])
plt.show()
#print(m_HP_file[0:365]*(T_supply-T_return)+(m_BTES*(T_supply)*eta))
#print((m_HP_file[0:365]*(T_supply-T_return)-m_BTES*(T_BTES)+m_BTES*(T_supply)))

#print(Heat_Load_file)
Peak_COP = max(COP)
Lowest_COP = min(COP)

print(Peak_COP)
print(Lowest_COP)
#print(COP)

print(sum(COP)/365)

#Power consumption
Not_absolute_power_consumption_HP = Heat_Load_file/(COP*1000)/24/3600
Power_consumption_HP = abs(Heat_Load_file/(COP*1000)/24/3600)

ax = plt.subplot(1,1,1)
#plt.plot(Power_consumption_HP[0:8761])
plt.plot(Power_consumption_HP[0:365])
#plt.xticks([0,730,1460,2190,2920,3650,4380,5110,5840,6570,7300,8030,8760])
plt.xticks([0,31,59,90,120,151,181,212,243,273,304,334,365])
ax.set_xticklabels(['Jan.','Feb.','March','April','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.','Jan.'])
plt.ylabel("Power Consumption (kW)")
plt.xlabel("Time")
plt.title('Power Consumption of Heat Pump in 2019')
plt.show()

peak_power_consumption_HP = max(Power_consumption_HP)
peak_power_consumption_HP_cooling = max(Not_absolute_power_consumption_HP)
print(peak_power_consumption_HP)
print(peak_power_consumption_HP_cooling)


#Reinjection Temperature
T_reinjection = T_supply - (eta*(T_supply+273.15)/COP[0:365])
#print(T_reinjection)

c = {'mass_flow_rate': np.array(abs(m_HP[:,0])),'COP_heat_demand': np.array(abs(COP[:,0])),'Power Consumption':np.array(abs(Power_consumption_HP[:,0])),'T_Reinjection':np.array(abs(T_reinjection[:,0]))}
dfc = pd.DataFrame(data=c)
dfc.to_csv("COPheatdemand.csv")

print(np.average(T_reinjection))

