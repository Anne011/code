#Overall borehole Thermal Resistance
import numpy as np
import math

#initialisation
lamda_grout = 3.7 #thermal conductivity of grout [W/m.k]
lamda_tube = 0.544 #thermal conductivity of U-tube [W/m.k]
k = 2.5 #thermal conductivity of rock/soil [W/m.k]
h = 5400 #conductive heat transfer coefficient [W/m^2.K] *****
D = 60*10**(-3) #shank spacing between centers [m]
d_i = 13.1*10**(-3) #inner diameter of U-tube [m]
d_o = 16*10**(-3) #outer diameter of U-tube [m]
d_b = 0.13 #borehole diameter [m]
r_borehole = 0.065 #borehole radius [m]
alpha = 1.0416*10**(-6) #thermal diffusitivity of soil [m^2/s]

#R_b = R_grout + R_pipewall +- R_convection 【m.k/W】
R_grout = 1/(2*np.pi*lamda_grout)*(math.log(d_b/d_o)+math.log(d_b/D)+((lamda_grout-k)/(lamda_grout+k)*math.log(d_b**4/(d_b**4-D**4))))
R_pipewall = 1/(2*np.pi*lamda_tube)*math.log(d_b/d_o)
R_convection = 1/(np.pi*d_i*h)
R_b = R_grout + R_pipewall + R_convection

print(R_b)