#Program3B3
#J. Austin Christensen
#Purpose:
#   This program simulates a set of random dice rolls and tracks the largest 
#   roll in each set, then prints the largest at the end of the set.
#    
#    
#
#2022-09-19

import random


#variables
numDice = 2
numSides = 6
numRolls = 5
result = 0
rollTotal = 0
highRoll = 0
highRollTotal = 0

#explain the program to the user
print("This program simulates a set of random dice rolls and tracks the largest " +
        "roll in each set, then prints the largest at the end of the set." +
        "" +
        "\n")

#get inputs for number of dice, number of sides, number of rolls
numDice = int(input("Enter the number of dice: "))
numSides = int(input("Enter the number of sides: "))
numRolls = int(input("Enter the number of rolls: "))
print("")

#print header for results table
print("%-10s" % ("Roll#"), end = "")  
for die in range(1, numDice + 1):
    header = "Die " + str(die)
    print("%-10s" % (header), end = "")
print("%-10s" % ("Total"), end = "")  
print("")

#simulate rolls and print results
for roll in range(1, numRolls + 1):
    print("%-10d" % roll, end = "")

    #roll each die in the set, add to the total, print the result
    for die in range(1, numDice + 1):
        result = random.randint(1, numSides)
        rollTotal += result
        print("%-10d" % result, end = "")
    print("%-10d" % rollTotal, end = "")

    #check if the roll was the higest so far and save it if so
    if rollTotal >= highRollTotal:
        highRoll = roll                                    
        highRollTotal = rollTotal
        print("*", end = "")
        
    #reset the roll total to zero for each new roll and start a new line
    rollTotal = 0
    print("")

#print the highest roll
print("")
print("The last high roll of %d rolls was roll %d with a total of %d" % (numRolls, highRoll, highRollTotal)) 
    
