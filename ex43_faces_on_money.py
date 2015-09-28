# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 43
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 43: Faces on Money

print "Insert denomination of a banknote:"
denom = int(raw_input("> "))

if denom == 1:
	name = "George Washington"
elif denom == 2:
	name = "Thomas Jefferson"
elif denom == 5:
	name = "Abraham Lincoln"
elif denom == 10:
	name = "Alexander Hamilton"
elif denom == 20:
	name = "Andrew Jackson"
elif denom == 50:
	name = "Ulysses S. Grant" 
elif denom == 100:
	name = "Benjamin Franklin"
else:
	print "The denomination doesn't exist."
	exit()

print "The face on the $%i banknote is that of %s." % (denom, name)