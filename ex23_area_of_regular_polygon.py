# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 23
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 23: Area of a Regular Polygon

from math import tan, pi

print "Enter the length of a side:"
s = float(raw_input("> "))

print "Enter the number of sides:"
n = int(raw_input("> "))

area = n * (s ** 2) / (4 * tan(pi / n))

print "The area of the polygon is", area