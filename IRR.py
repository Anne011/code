import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
k=[]
NPV=[]
for i in range(600,2100,1):
    k.append(i/10000)
    Initial_investment = 12.29908
    annual_income = 1.98844  #72761
    annual_cost = Initial_investment/100
    year = []
    year = np.zeros(27)
    year[26] = 27
    discount_rate1 = i/10000

    npv1 = np.zeros(27)
    npv1[1] = -Initial_investment

    for j in range(1,26,1):
        year[j]=j
        annual_change=(annual_income-annual_cost)/(discount_rate1+1)**j
        npv1[j+1]=npv1[j]+annual_change
    NPV.append(npv1[26])
    if npv1[26]<0:
        print(discount_rate1)

ref_line = np.zeros(1500)
#print(NPV)
#NPV /= 10^(-6) #unsupported operand type(s) for ^: 'list' and 'int'
#print(k)

plt.plot(k,NPV)

plt.plot(k,ref_line,'y--')
plt.plot(0.1468,0,'.m')
plt.xlabel('Discount rate')
plt.ylabel('Net present value (*10^5 GBP)')
plt.legend(['Net present value','Internal rate of return = 0.147'])
#plt.title('Net Present Value vs Discount Rate' )
plt.show()

