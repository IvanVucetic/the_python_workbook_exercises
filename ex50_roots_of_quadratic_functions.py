# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 50
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 50: Roots of a Quadratic Function

from math import sqrt

print "For quadratic function (a * x^2) + b*x + c"
print "insert a, b and c:"
a = float(raw_input("a: "))
b = float(raw_input("b: "))
c = float(raw_input("c: "))

roots = []

# evaluate discriminant
discriminant = b**2 - 4*a*c

if discriminant > 0:
    num_roots = 2
    x1 = ((-b) + sqrt(discriminant)) / 2*a
    x2 = ((-b) - sqrt(discriminant)) / 2*a
    print "There are 2 roots: %f and %f" % (x1, x2)
elif discriminant == 0:
    num_roots = 1
    x = (-b) / 2*a
    print "There is one root: ", x
else:
    num_roots = 0
    print "No roots, discriminant < 0."
    exit()

