import random
import numpy as np

#Tie one on
max_customers = 10000
ST = np.random.normal(6 , 1 , 10000)    #Service Time clerk.
sales  = []     #Sales from each customer
AT = []         #Arrival time
WT = []         #Wating time.
W_Cost = []     #Wating Cost.
CT = []         #Completion Time.(start service[i] + service time[i])
ServiceStartTime = [] #Service Start Time to have customer to clerk(Like ATM)
Profit1 = 0 
Profit2 = 0

for i in range (1,3):
    if  i == 1 :    #Shop 1
        SATArray = [0,0]        #Server Avail Time Array --- completion time
        SSATArray = [0,0,0]     #System Space Avail Time Array -- Customer
    else :          #Shop 2
        SATArray = [0,0,0,0,0,0]                    #Server Avail Time Array
        SSATArray=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]   #System Space Avail Time Array
    for c in range (max_customers):
        IAT = np.random.normal( 1.5 , 0.15 )    #Inter arrival time.
        if c > 1:
            AT.append(IAT + AT[c-1])
        else :
            AT.append(IAT)
        if AT[c] > 10*60 :          #if time > 10 hours (open hours)
            break                   #no more customers will be taken
        
        position =np.argmin(SSATArray)         #position of the smallest completion time of all chairs
        
        if AT[c] < SSATArray[position] :    #Customer left.
            WT.append(0)    
            sales.append(0)
            CT.append(0)
            W_Cost.append(0)
            ServiceStartTime.append(0)
            continue
        
        sales.append(22)                    #if customer entered he will pay
        position2=np.argmin(SATArray)       #position of the smallest completion of all clerks
        ServiceStartTime.append(max(AT[c],SATArray[position2]))#supposed when clerk works on my clothes
        WT.append(ServiceStartTime[c]-AT[c])#Wating time of each customer.          
        W_Cost.append(WT[c]*(10/60))        #how much will i pay for waiting customer.
        CT.append(ST[c] + ServiceStartTime[c])   #Service time + smallest value in clerks array.    
        SATArray[position2] = CT[c]         #New Completion time of new clerk.
        SSATArray[position] = CT[c]         #New Completion time of new clerk.
        
    #Profit of first shop(small)   
    if(i==1):
        Profit1 = sum(sales ) - sum(W_Cost) 
        Profit1 = Profit1 - 200-(20*3*10)
    else:
        Profit2 = sum(sales ) - sum(W_Cost)
        Profit2 = Profit2 - 2000-(20*6*10)
        
if Profit1 > Profit2:
    print('use the first configuration')
else :
    print('use the second configuration')
        
                        








    
