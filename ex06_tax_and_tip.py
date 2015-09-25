# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 6
# Date: 24.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 6: Tax and Tip

print "Tell me the price of your meal"
meal = float(raw_input("> "))

tax = meal * 0.21
tip = meal * 0.18
sum_ = meal + tax + tip

print "The tax on your meal is $%.2f." % tax
print "The tip on your meal is $%.2f." % tip
print "You should pay a total of $%.2f." % sum_

