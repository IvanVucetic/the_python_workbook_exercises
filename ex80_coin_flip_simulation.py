# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 80
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 80: Coin Flip Simulation

from random import random

total_flips = 0

for i in range(10):
    streak = []
    counter = 0
    while True:
        x = random()
        result = "H" if x < 0.5 else "T"
        print result,
        counter += 1
        if len(streak) == 0:
            streak.append(result)
        else:   
            if result != streak[-1]:
                streak = []
                streak.append(result)
            else:
                streak.append(result)
                if len(streak) == 3:
                    break
                else:
                    pass
    print "(%s flips)" % counter
    total_flips += counter

print "On average, %.1f flips were made." % (total_flips / 10.0)