# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 16
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 16: Area and Volume

from math import pi

while True:
	print "Insert the radius:"
	r = float(raw_input("> "))
	if r > 0: 
		break

print "Area of the circle is", round((r ** 2) * pi, 2)
print "Volume of the sphere is", round((4.0 / 3) * (r ** 3) * pi, 2)