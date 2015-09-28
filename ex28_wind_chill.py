# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 28
# Date: 27.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 28: Wind Chill

import math

print "Please enter the air temperature in degrees Celsius:"
t = float(raw_input("> "))

print "Please enter the wind speed in kilometers per hour:"
v = float(raw_input("> "))

wci = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)

print "The wind chill index is", int(round(wci, 0))