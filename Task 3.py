import random

#Determinestic Inputs
ShortageCost = 100
HoldingCost = 50
SellingPrice = 450

#lists
profitlist = list()     #Profit List
x= list()          #Demands
#AverageProfit1 = 0
#AverageProfit2 = 0

def random_0to1():
    return random.uniform(0, 1)

def get_x():
  rand_prob=random_0to1()
  if rand_prob>=0 and rand_prob<0.2:
       x=0
  elif rand_prob>=0.2 and rand_prob<0.6:
       x=1                              
  elif rand_prob>=0.6 and rand_prob<0.8:
       x=2
  elif rand_prob>=0.8 and rand_prob<0.9:
       x=3
  else :
       x=4
  return x

for i in range (500) :      #i is the Order
    x.append(get_x ())

for Order in range (1,3) :         #Order is 1 or 2
    Avail = 1
    for Week in range (500) :   #500 Week
        Avail += Order
        if x[Week]< Avail :
            sold = x[Week]
            Avail -= x[Week]
            loss = Avail * HoldingCost
        elif x[Week] > Avail :
            sold = Avail
            Avail = 0
            loss = (x[Week] - sold) * ShortageCost
        else :
            sold = x[Week]
            Avail = 0
            loss = 0
        revenue = sold * SellingPrice 
        profit = revenue - (loss)
        if profit >= 0 :
            profitlist.append(profit)
    if Order == 1 :
        AverageProfit1 = sum(profitlist) / 500
        profitlist.clear()
    else :
        AverageProfit2 = sum(profitlist) / 500


#Printing Information:

print ("The average profit of 500 weeks :" , "\n")
print ("if the shop owner ordered 1 PC per week :" , AverageProfit1 ,"\n" )
print ("if the shop owner ordered 2 PC per week :" , AverageProfit2 ,"\n" )

if AverageProfit1 > AverageProfit2 :
    print("Ordering 1 PC per week is the best decision")
elif AvgProfit1 < AvgProfit2:
    print("Ordering 2 PC per week is the best decision")
        
