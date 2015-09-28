# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 35
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 35: Dog Years

print "Enter a dog's age in human years:"
hy = int(raw_input("> "))

if hy < 0:
	print "Error, must be positive number."
	exit()
elif hy <= 2:
	dy = hy * 10.5
else:
	dy = 21 + (hy - 2)*4

print "The dog's age in dog's years is", dy
