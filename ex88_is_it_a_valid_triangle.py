# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 88
# Date: 03.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 88: Is it a Valid Triangle?

def validate_triangle(a,b,c):
	if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
		return True
	else:
		return False


print "Validate triangle by inserting length of its sides:"
a1 = float(raw_input("a: "))
b1 = float(raw_input("b: "))
c1 = float(raw_input("c: "))

if validate_triangle(a1,b1,c1):
	print "The triangle is valid."
else:
	print "The triangle is not valid."