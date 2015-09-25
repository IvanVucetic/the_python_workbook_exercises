# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 22
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 22: Area of a Triangle (Again)

from math import sqrt

print "Enter the length of the first side:"
s1 = float(raw_input("> "))

print "Enter the length of the second side:"
s2 = float(raw_input("> "))

print "Enter the length of the third side:"
s3 = float(raw_input("> "))

s = (s1 + s2 + s3) / 2

area = sqrt(s * (s - s1) * (s - s2) * (s -s3))

print "The area of the triangle is", round(area, 2)