# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 81
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 81: Compute the Hypotenuse

from math import sqrt

def hypotenuse(a,b):
	c = sqrt(a**2 + b**2)
	return c

print "Insert lengths of shorter triangle sides:"
a_side = float(raw_input("a: "))
b_side = float(raw_input("b: "))

c_side = hypotenuse(a_side, b_side)

print "The length of the hypotenuse is", c_side 
