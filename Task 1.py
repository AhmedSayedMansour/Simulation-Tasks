#Libraries
import random
import numpy as np
import matplotlib.pyplot as plt
#________________________________________
# deterministic input
Selling_Price = 249
Administrative_Cost = 400000
Advertising_Cost  = 600000
totalFixedCost = Advertising_Cost + Administrative_Cost

#Inputs_________________________________________________
count = 10**6
mu ,Sigma = 15000,4500

#_____________________________________________
#lists to draw histogram

#list of numbers generated randomly (C1)
directCost = list()
#list of numbers generated randomly (C2)
partsCost = list()
#list of numbers generated randomly (x)
Demand = list()
#list of profit values
ProfitList = list()

#____________________________________________________________
#calculating C1,C2,X values with functions in terms of probability of each range
def random_0to1():
    return random.uniform(0, 1)

def get_c1():
  rand_prob=random_0to1()
  if rand_prob>=0 and rand_prob<0.1:
       c1=43
  elif rand_prob>=0.1 and rand_prob<0.3:
       c1=44                               
  elif rand_prob>=0.3 and rand_prob<0.7:
       c1=45
  elif rand_prob>=0.7 and rand_prob<0.9:
       c1=46
  else :
       c1=47
  return c1

def get_c2():
    c2 = random.uniform(80,100)
    return c2

def get_x():
    x = np.random.normal(15000,4500)
    return x

#_____________________________________________________
#Array to get Lists with range of num of probabilities
loss = 0
Max = 0
Min = 0

for i in range(count) : 
    #counting number of trials to get average
    c1 = get_c1() 
    directCost.append(c1)
    c2 = get_c2()
    partsCost.append(c2)
    x = get_x()
    Demand.append(x)
    profit = (( 249 - c1 - c2 )*x) - 1000000
    if profit < 0 :
        #ProfitList.append(profit)
        loss = loss + 1
    else :
        ProfitList.append(profit)
    Max = max(profit,Max)
    Min = min(profit,Min)

# ________________________________________
#Outputs

print("Maximum Profit = ", Max, "\n")
print("Minimum Profit = ", Min, "\n")
print("Average Profit = ", sum(ProfitList)/len(ProfitList),"\n")
print("Probability of Loss = ", loss/count, "\n")
print("Probability of profit = ",1-(loss/count),"\n")

#_________________________________________________
#Plots the graphs

plt.hist(directCost, density = True , bins = 30)
plt.ylabel('probability of c1')
plt.xlabel('Values of c1')
plt.show()

plt.hist(partsCost, density = True, bins = 30)
plt.ylabel('probability of c2')
plt.xlabel('Values of c2')
plt.show()

plt.hist(Demand, density = True, bins = 30)
plt.ylabel('probability of x')
plt.xlabel('Values of x')
plt.show()

plt.hist(ProfitList , density = True , bins = 30)
plt.ylabel('probability of profit')
plt.xlabel('Values of the Profit')
plt.show()


        
