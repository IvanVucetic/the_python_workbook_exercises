# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 9
# Date: 24.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 9: Compound Interest

print "Amount of money to deposit:"
deposit = float(raw_input("> "))

# interest rate is 4%

savings1 = deposit * 1.04
savings2 = savings1 * 1.04
savings3 = savings2 * 1.04

print "The amount in the savings after 1 year is $%.2f" % savings1
print "The amount in the savings after 2 years is $%.2f" % savings2
print "The amount in the savings after 3 years is $%.2f" % savings3


# universal solution:
# each year, savings are deposit * (1.04 ^ years)
# e.g. y2 - deposit * 1.04 * 1.04 (i.e. y1 * 1.04)
# 	   y3 - deposit * 1.04 * 1.04 * 1.04
