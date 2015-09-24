# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 5
# Date: 24.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 5: Bottle Deposits

print "Tell me the number of bottles smaller or equal to 1 litre"
a = int(raw_input("> "))
print "Tell me the number of bottles larger than 1 litre"
b = int(raw_input("> "))

refund = a * 0.10 + b * 0.25
print "Your refund is $%.2f." % refund

# %.2f --- format as a float with 2 decimal places
# .x is a 'precision'