# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 18
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 18: Volume of a Cylinder

from math import pi

print "Insert the radius of the cylinder's base:"
r = float(raw_input("> "))

print "Insert the height of the cylinder:"
h = float(raw_input("> "))

volume = (r ** 2) * pi * h
print "The volume of the cylinder is %.1f." % volume

