# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 63
# Date: 30.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 63: Temperature Conversion Table

print "Celsius, Fahrenheit"
for i in range(0, 101, 10):
	print "%5i %9i" % (i, i * 9/5 + 32)
	# used number after % to better align to heading