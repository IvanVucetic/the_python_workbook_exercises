# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 40
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 40: Name that Triangle

print "Enter lengths of the triangle sides:"
a = int(raw_input("a: "))
b = int(raw_input("b: "))
c = int(raw_input("c: "))

if a == b == c:
	print "Equilateral triangle"
elif a != b != c:
	print "Scalene triangle"
else:
	print "Isoscales triangle"