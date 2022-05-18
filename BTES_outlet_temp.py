# BTES outlet temperature

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

C_soil_wet = 1480 #J/(kgK)
V_soil = 14402*2 #m^3
#V_soil = 14402 #m^3
Rho_soil_wet = 1760 #kg/m^3
m_soil = Rho_soil_wet * V_soil #kg
T_inlet_BTES_day0 = 12 #degree celcius
T_BTES = 30 #degree celcius initial ground temperature is 12
Q_store_day0 = C_soil_wet*m_soil*(T_BTES-T_inlet_BTES_day0)
#Q_store_day0 = C_soil_wet*m_soil*(40-12)
eta_system = 0.42
#print(m_soil)

Q_out_building = pd.read_csv("/Users/angelchen/Desktop/讲义/Year3/3YP/code/heat_load_J_new.csv", usecols=[1]).values
print(Q_out_building[0])
Q_in_from_BTES = np.zeros(shape = (365,1))
Temp_changei = np.zeros(shape = (365,1))
Temp_out_BTES = np.zeros(shape = (365,1))
Temp_into_BTES = np.zeros(shape = (365,1))

#print(Q_store_dayi)
i = 1 #day1
j = 1
Q_store_dayi = np.zeros(shape = (366,1))
Q_store_dayi[0,0] = Q_store_day0 #+
#Q_out_building[1]


#while j < 366:
while i < 366:
    if i <= 365: #or i > 273: #inject heat from CT
        Q_in_from_BTES[i-1,0] = Q_out_building[i-1]*(1-1/4) #(1-eta_system)
        Q_store_dayi[i,0] = Q_store_dayi[i-1,0] + Q_in_from_BTES[i-1,0] # + Q[i,0]
        #print(Q_store_dayi)
        #
        Q_store_dayi[i,0] = 0.998*Q_store_dayi[i,0] #+ 6.048e9 #comes from the 0.42 efficiency
        Temp_changei[i-1,0] = Q_store_dayi[i,0]/(C_soil_wet*m_soil)
        #Temp_out_BTES[i-1,0] = T_BTES + sum(Temp_changei[0:i,0]) - (i-1)*4 -i*(T_BTES - (T_inlet_BTES_day0+4))
        Temp_out_BTES[i-1,0] = T_inlet_BTES_day0 + Temp_changei[i-1,0]
        #print(sum(Temp_changei[0,0:i]))
        Temp_into_BTES[i-1,0] = Temp_out_BTES[i-1,0] - 10 #Constant difference of 10 degree
        # #print(Temp_changei)
        i += 1
        # end
    else:
        Q_in_from_BTES[i - 1, 0] = Q_out_building[i - 1] / (1 - eta_system)
        Q_store_dayi[i, 0] = Q_store_dayi[i - 1, 0] + Q_in_from_BTES[i - 1, 0] #+ 6.912e9
        #Q_store_dayi[i, 0] = 0.998 * Q_store_dayi[i, 0] #+ 6.048e9 #+ 8640000000 # comes from the 0.42 efficiency gain!
        Temp_changei[i - 1, 0] = Q_store_dayi[i, 0] / (C_soil_wet*m_soil)
        Temp_out_BTES[i - 1, 0] = T_inlet_BTES_day0 + Temp_changei[i - 1, 0]
        Temp_into_BTES[i - 1, 0] = Temp_out_BTES[i - 1, 0] - 10  # Constant difference of 10 degree
        i += 1



#print(Temp_changei)
#print(sum(Temp_changei[0,0:2]))
print(Temp_out_BTES)
#print(Q_store_dayi)
#print(Q_in_from_BTES)


#c = {'Temp_out_BTES': np.array(Temp_out_BTES[:,0]),'Temp_into_BTES': np.array(Temp_into_BTES[:,0]),'Q_in_ground':np.array(Q_store_dayi[:,0])}
#dfc = pd.DataFrame(data=c)
#dfc.to_csv("inlet_outlet_temp_BTES.csv")
