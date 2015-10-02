# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 77
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 77: Binary to Decimal

print "Insert a binary number to convert it to decimal:"
binary = list(raw_input("> "))
value = 0

for i in range(len(binary)):
	digit = binary.pop()
	if digit == '1':
		value = value + pow(2, i)

print "The decimal value of the number is", value