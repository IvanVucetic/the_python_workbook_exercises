# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 37
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 37: Name that Shape

print "Enter number of sides of a geometric shape:"
sides = int(raw_input("> "))

if sides < 3 or sides > 10:
	print "Must be a number between 3 and 10."
elif sides == 3:
	print "It's a triangle."
elif sides == 4:
	print "It's usually a square or a rectangle."
elif sides == 5:
	print "It's a pentagon."
elif sides == 6:
	print "It's a hexagon."
elif sides == 7:
	print "It's a heptagon."
elif sides == 8:
	print "It's an octagon."
elif sides == 9:
	print "It's a nonagon."
elif sides == 10:
	print "It's a decagon."
