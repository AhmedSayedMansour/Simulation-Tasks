#Used Method : Linear congruential Generator

seed = 12345    #intial value

def PRNG() :            #Pseudocode random Number Generator
    global seed
    seed = 12354*seed + 79841
    return (seed%1000)/1000.0

#Printing Values.
for i in range (100) :
    print (PRNG() , "\n")
