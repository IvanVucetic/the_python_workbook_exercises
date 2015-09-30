# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 69
# Date: 30.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 69: Approximate pi

pi = 3.0
sign = 1

print pi

for i in range(1, 16):
	add = (4.0 / (2*i * (2*i + 1) * (2*i + 2))) * sign
	pi += add
	print i, ":", pi
	sign = sign * (-1)