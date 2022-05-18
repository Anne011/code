#Year 0 temp

import numpy as np
import pandas as pd

i = 1
#day1 of Year0
m_CT = 2.1 #kg/s
Cp_water = 4180 #J/kgK
T_out_BTES_day1 = 12 #degree celsius
working_time = 15*3600 #s
#ground
C_soil_wet = 1480 #J/(kgK)
V_soil = 14402*2 #m^3
Rho_soil_wet = 1760 #kg/m^3
m_soil = Rho_soil_wet * V_soil #kg
Q_need = C_soil_wet*m_soil*(40 - T_out_BTES_day1) #total heat we need to store in year0


Q_in_ground_from_CT = np.zeros(shape = (365,1))
T_out_BTES = np.zeros(shape = (366,1))
Energy_stored_dayi = np.zeros(shape = (365,1))
Temp_change_dayi = np.zeros(shape = (365,1))

T_out_BTES[0,0] = T_out_BTES_day1

#Q_day1 = m_CT*Cp_water*(50-T_out_BTES_day1)
#Energy_stored_day1 = Q_day1*working_time

#Temp_change_day1 = Energy_stored_day1/C_soil_wet/m_soil
#print(T_out_BTES)


while i < 366:
    Q_in_ground_from_CT[i-1,0] = m_CT*Cp_water*(50-T_out_BTES[i-1,0])
    Energy_stored_dayi[i-1,0] = Q_in_ground_from_CT[i-1,0]*working_time #*0.998 #0.998 comes from the 0.42 efficiency
    Temp_change_dayi[i-1,0] = Energy_stored_dayi[i-1,0]/C_soil_wet/m_soil
    T_out_BTES[i,0] = T_out_BTES[i-1,0]+Temp_change_dayi[i-1,0]
    i += 1


print(T_out_BTES)

