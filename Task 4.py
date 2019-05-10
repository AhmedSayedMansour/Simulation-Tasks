import random
import numpy as np

#Inter Arrival Time
IAT = np.random.exponential(1 , 10**6)#Array contains random exponential numbers with mean = 1
AT = [] #Arrival Time
SST = [] #Start Service Time
WT = [] #Waiting Time
CT = [] #Completion Time
TIS = [] #Time in System

#Service Times for the three ATMs
ST1 = np.random.randint(2, 4, 10**6)#unifrom distribution of ATM1 (min=2,max=4)
ST2 = []
for i in range(10**6):
    z = random.triangular(2,4,3.3)#triangular distribution (a=2 , b=4 , c=3.3)
    ST2.append(z)
ST3 = np.random.normal(3,0.5,10**6)#normal distribution (mean =3 ,standard deviation =0.5)

#arrays of the three ATMs
ATM1 = []
ATM2 = []
ATM3 = []

for i in range(10**6):
    if(i == 0):             #First ROW (Client)
        AT.append(IAT[i])
        SST.append(IAT[i])
        WT.append(0)
        CT.append(SST[i] + ST1[i])
        TIS.append(CT[i] - AT[i])
        ATM1.append(CT[i])
        ATM2.append(0)
        ATM3.append(0)
        ST2[i]=0
        ST3[i]=0
    else:
        AT.append(AT[i-1] + IAT[i])
        SST.append(max(AT[i],min(ATM1[i-1],ATM2[i-1], ATM3[i-1])))
        WT.append(SST[i]-AT[i])
        if min(ATM1[i-1],ATM2[i-1], ATM3[i-1])== ATM1[i-1]:
            CT.append(SST[i] + ST1[i])
            ATM1.append(CT[i])
            ATM2.append(ATM2[i-1])
            ATM3.append(ATM3[i-1])
            ST2[i]=0
            ST3[i]=0
        elif min(ATM1[i-1],ATM2[i-1], ATM3[i-1])== ATM2[i-1]:
            CT.append(SST[i] + ST2[i])
            ATM2.append(CT[i])
            ATM1.append(ATM1[i-1])
            ATM3.append(ATM3[i-1])
            ST1[i]=0
            ST3[i]=0
        else:
            CT.append(SST[i] + ST3[i])
            ATM3.append(CT[i])
            ATM2.append(ATM2[i-1])
            ATM1.append(ATM1[i-1])
            ST1[i]=0
            ST2[i]=0
        TIS.append(CT[i] - AT[i])

#Utilization for each ATM = TOTAL SERVICE TIME / TOTAL TIME OF SIMULATION
UTI1 = sum(ST1)/max(ATM1)
UTI2 = sum(ST2)/max(ATM2)
UTI3 = sum(ST3)/max(ATM3)

#Average Waiting Time
AvgWT = sum(WT)/(10**6)

#Maximum Waiting Time
MaxWT = max(WT)

#probability of Waiting
Wait1M = 0 #Number of people waiting more than one minute
Wait = 0 #Number of people waited
for i in range (10**6):
    if (WT[i] > 1):
        Wait1M = Wait1M + 1
    if (WT[i] > 0):
        Wait = Wait + 1
ProbofWait1M = (Wait1M/10**6)*100 #probability of Waiting more than one minute
ProbofWait   = (Wait/10**6)*100   #probability of Waiting


print("Utilization of ATM1: ",UTI1, "\n")
print("Utilization of ATM2: ",UTI2, "\n")
print("Utilization of ATM3: ",UTI3, "\n")
print("Average waiting time: ",AvgWT,"\n")
print("Maximum waiting time: ",MaxWT,"\n")
print("probability of waiting time: ",ProbofWait,"\n")
print("probability of waiting more than 1 minute: ",ProbofWait1M,"\n")


