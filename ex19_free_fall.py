# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 19
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 19: Free Fall

from math import sqrt

print "Enter the height from which the object is dropped (m):"
d = float(raw_input("> "))

v_init = 0 # m/s; since == 0, not needed
a = 9.8 # m/s^2

v = sqrt(2 * a * d)
print "The final speed at the moment of impact is %.2f meters per second" % v
