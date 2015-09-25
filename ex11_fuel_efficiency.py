# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 11
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 11: Fuel Efficiency

print "What is the fuel efficiency in miles per gallon?"
mpg = float(raw_input("> "))

lp100km = 235.238 / mpg

print "The fuel efficiency is %.1f liters per 100km." % lp100km