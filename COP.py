# COP wrt time of the whole system
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.optimize import fsolve
Heat_Load_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/heat_load_J.csv", usecols=[1]).values

Cp = 4200 #Jouls/(kg*degree)
T_supply = 70 #degree
T_return = 50 #degree
second_in_day = 24*3600 #s
m_BTES = 3.7 #kg/s
eta = 0.42 #fraction of Carnot Cycle
T_BTES = 42.6 #degree

#mass flow rate in HP
ax = plt.subplot(1,1,1)
m_HP = Heat_Load_file[0:365]/(Cp*(T_supply - T_return)*second_in_day)
m_HP_peak_cooling = max(m_HP)
m_HP_peak_heating = max(abs(m_HP))

plt.plot(abs(m_HP[0:365]))
plt.xticks([0,30.17,60.33,90.5,120.67,150.83,181,211.17,241.33,271.5,301.67,331.83,362])
ax.set_xticklabels(['Jan.','Feb.','March','April','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.','Jan.'])
plt.ylabel("Mass Flow Rate in HP (kg/s)")
plt.xlabel("Time")
plt.show()

print(m_HP_peak_cooling)
print(m_HP_peak_heating)
#print(m_HP)

#special = np.array([1,2,3,4,5]).T

#def solve_COP():
#for i in range((1,5,1)):
    #special = np.zeros(4,1)
    #special[i] = np.array(m_HP[i]*(T_supply-T_return)).reshape(4,1)

    #print(special[0,i])
    #return[
        #special[i]
            #[cop]=(special[i]+m_BTES*(T_supply+273)*eta)/(special[i]-m_BTES*(T_BTES+273)+m_BTES*(T_supply+273))
        #]

#print(cop)
#print(special[i])


#COP
m_HP_file = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/heat_load_J.csv", usecols=[3]).values
#print(m_HP_file)
ax = plt.subplot(1,1,1)
#star = m_HP_file[0:365]*(T_supply-T_return)
COP = (m_HP_file[0:365]*(T_supply-T_return)+(m_BTES*(T_supply+273)*eta))/(m_HP_file[0:365]*(T_supply-T_return)-m_BTES*(T_BTES+273)+m_BTES*(T_supply+273))
#COP = (m_HP_file[0:365]*(T_supply-T_return)+(m_BTES*(T_supply)*eta))/(m_HP_file[0:365]*(T_supply-T_return)-m_BTES*(T_BTES)+m_BTES*(T_supply))
#print(COP)
#COP = (m_HP_file[0:365]*(T_supply-T_return)+1)
plt.plot(COP[0:365])
plt.xticks([0,30.17,60.33,90.5,120.67,150.83,181,211.17,241.33,271.5,301.67,331.83,362])
ax.set_xticklabels(['Jan.','Feb.','March','April','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.','Jan.'])
plt.ylabel("COP of the Whole System")
plt.xlabel("Time")
plt.show()
#print(m_HP_file[0:365]*(T_supply-T_return)+(m_BTES*(T_supply)*eta))
#print((m_HP_file[0:365]*(T_supply-T_return)-m_BTES*(T_BTES)+m_BTES*(T_supply)))

Peak_COP = max(COP)
Lowest_COP = min(COP)

print(Peak_COP)
print(Lowest_COP)
#print(COP)

#energy input
Energy_input_to_HP = abs(Heat_Load_file/COP)
ax = plt.subplot(1,1,1)
plt.plot(Energy_input_to_HP[0:365])
plt.xticks([0,30.17,60.33,90.5,120.67,150.83,181,211.17,241.33,271.5,301.67,331.83,362])
ax.set_xticklabels(['Jan.','Feb.','March','April','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.','Jan.'])
plt.ylabel("Energy input to HP(J)")
plt.xlabel("Time")
plt.show()

peak_Energy_input_to_HP = max(Energy_input_to_HP)
print(peak_Energy_input_to_HP)
#print(Energy_input_to_HP)
#370706041118

#Power consumption
Power_consumption_HP = abs(Heat_Load_file/(COP*second_in_day*1000))
ax = plt.subplot(1,1,1)
plt.plot(Power_consumption_HP[0:365])
plt.xticks([0,30.17,60.33,90.5,120.67,150.83,181,211.17,241.33,271.5,301.67,331.83,362])
ax.set_xticklabels(['Jan.','Feb.','March','April','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.','Jan.'])
plt.ylabel("Power Consumption in HP (kW)")
plt.xlabel("Time")
plt.show()

peak_power_consumption_HP = max(Power_consumption_HP)
print(peak_power_consumption_HP)