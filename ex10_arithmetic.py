# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 10
# Date: 24.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 10: Arithmetic

from math import log10

a = int(raw_input("Insert number A: "))
b = int(raw_input("Insert number B: "))

print "A + B =", a + b
print "A - B =", a - b
print "A * B =", a * b
print "A / B =", a / b
print "remainder to A / B =", a % b
print "base-10 logarithm of A is ", log10(a)
print "A to the power B =", a ** b
