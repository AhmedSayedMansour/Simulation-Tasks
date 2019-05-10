import numpy as np
import random
import statistics as sst 


#******Casher*****#

MaxCustomers = 2000

IAT = np.random.normal( 1.0 ,0.2 , MaxCustomers)
ST_Casher = np.random.normal ( 4/6 , 1/6 , MaxCustomers)    #Casher Servise time to collect money

AT = list()
TS_Casher = list()      #Time Spend in the machine(complation Time - arrival time)
CT_Casher = list()      #complation Time of each customer

for i in range (0 , MaxCustomers):
    if i == 0 :
        AT.append(IAT[0])
        CT_Casher.append(ST_Casher[0])
        TS_Casher.append(ST_Casher[0])
    else:   
        AT.append(IAT[i] + AT[i-1])
        startservisetime = max(AT[i],CT_Casher[i-1])        #max is the start servise
        CT_Casher.append(startservisetime+ ST_Casher[i])    #Complation time
        TS_Casher.append(CT_Casher[i]- AT[i])               #Time Spend

AVG_TS_Casher = sst.mean(TS_Casher)

#******Salad******#

SaladLines  = [ 0 , 0 , 0 , 0 ]     #Complation Time of each line
ST_Salad  = np.random.normal ( 2, 1/3 , MaxCustomers)    #Salad  Servise time to start in lines of soup
TS_Salad = list()      #Time Spend in the Salad line
CT_Salad = list()      #complation Time of each customer to have salad

for i in range (0 , MaxCustomers):
    position =np.argmin(SaladLines)  #position of lowest line that contains lowest number of customers
    starttime = max(CT_Casher[i] , min(SaladLines))
    CT_Salad.append(starttime + ST_Salad[i])
    SaladLines[position] = CT_Salad[i]
    TS_Salad.append(CT_Salad[i] - CT_Casher[i])

AVG_TS_Salad = sst.mean(TS_Salad)

#******Soup******#

Souprand = np.random.uniform(0,1, MaxCustomers)
N_Soup = 0
StartTime_Soup = list()             #start time to go to soup lines of people < 60%
for i in range (MaxCustomers):
    if(Souprand[i] <= 0.6):
        N_Soup = N_Soup + 1
        StartTime_Soup.append(CT_Salad[i])

SoupLines = [0,0]
ST_Soup = np.random.normal( 1 , 1/4 , N_Soup)   #Service Time in salad line
TS_Soup = list()      #Time Spend in the Soup line
CT_Soup = list()      #complation Time of each customer to have Soup

for i in range (N_Soup):
    position  = np.argmin(SoupLines)
    StartTime = max(StartTime_Soup[i] , min(SoupLines))
    CT_Soup.append(StartTime + ST_Soup[i])
    SoupLines[position] = CT_Soup[i]
    TS_Soup.append( CT_Soup[i] - StartTime_Soup[i])

AVG_TS_Soup = sst.mean(TS_Soup)

print('Average time a customer spends paying & getting food');
print('\nif getting salad only is: ', AVG_TS_Casher + AVG_TS_Salad );
print('\nif getting both is:', AVG_TS_Casher + AVG_TS_Salad + AVG_TS_Soup); 


    
    
    



