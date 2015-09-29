# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 60
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 60: Roulette Payouts

import random

print "The wheel is spinin'..."
num = random.randint(0,37)

print num

if num == 0:
    print "Pay 0"
elif num == 37:
    print "Pay 00"
elif num:
    print "Pay", num
    if num % 2 == 0:
        print "Pay even"
    else:
        print "Pay odd"
    if 1 <= num <= 18:
        print "Pay 1 to 18"
    else:
        print "Pay 19 to 36"
    if num in (1,3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, \
        32, 34, 36):
        print "Pay Red"
    else:
        print "Pay Black"