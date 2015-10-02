# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 71
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 71: Square Root

from math import pow

print "Insert number:"
x = float(raw_input("> "))
guess = x / 2

while abs(guess*guess - x) > pow(10, -12):
	guess = (guess + x/guess) / 2

print "Estimated square root of the number is", guess