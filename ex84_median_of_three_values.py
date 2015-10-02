# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 84
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 84: Median of Three Values

def median_of_three(a,b,c):
	if a > b:
		if a < c:
			median = a
		elif b > c:
			median = b
		else:
			median = c
	else:
		if a > c:
			median = a
		elif b < c:
			median = b
		else:
			median = c
	return median

print "Insert 3 numbers to find their median:"
a = float(raw_input("a: "))
b = float(raw_input("b: "))
c = float(raw_input("c: "))

print "The median is", median_of_three(a,b,c)
