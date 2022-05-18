import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Initial_investment= 1229908.00
annual_income=  198844.00
annual_cost= Initial_investment/100
#annual_cost=Initial_investment/100 #without justification (potentially: last over 100 years, so assume replace
#every 100 years (1366480-design cost) )
year=[]
year=np.zeros(27)
year[26]=27
discount_rate1=0.02
discount_rate2=0.03
#https://www.bpie.eu/wp-content/uploads/2015/10/Discount_rates_in_energy_system-discussion_paper_2015_ISI_BPIE.pdf
discount_rate3=0.06
npv1=np.zeros(27)
npv1[1]=-Initial_investment
npv2=np.zeros(27)
npv2[1]=-Initial_investment
npv3=np.zeros(27)
npv3[1]=-Initial_investment

for j in range(1,26,1):
        year[j]=j
        annual_change=(annual_income-annual_cost)/(discount_rate1+1)**j
        npv1[j+1]=npv1[j]+annual_change

for j in range(1,26,1):
        year[j]=j
        annual_change=(annual_income-annual_cost)/(discount_rate2+1)**j
        npv2[j+1]=npv2[j]+annual_change
        if npv1[j]>0:
            print(j)
#print(npv2)

for j in range(1,26,1):
        year[j]=j
        annual_change=(annual_income-annual_cost)/(discount_rate3+1)**j
        npv3[j+1]=npv3[j]+annual_change
#print(npv3)

ref_line = np.zeros(27)

lnpv1 = plt.plot(year,npv1)
lnpv2 = plt.plot(year,npv2)
lnpv3 = plt.plot(year,npv3)
plt.plot(year,ref_line,'y--')
plt.xlabel('Year')
plt.ylabel('Net Present Value')
plt.legend(['discount rate = 2%','discount rate = 3%','discount rate = 5%'])
#plt.title('Net Present Value vs Time')
plt.show()


print(npv2)
