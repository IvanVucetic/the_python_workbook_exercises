# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 83
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 83: Shipping Calculator

def shipping_costs(n):
	first = 10.95
	others = 2.95

	price = first + (n-1)*others
	return price

print "Insert a number of purchased items:"
num = int(raw_input("> "))

print shipping_costs(num)