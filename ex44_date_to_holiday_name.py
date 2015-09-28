# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 44
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 44: Date to Holiday Name

print "Enter month and day (e.g. 'January 1'):"
date = raw_input("> ")

if date == 'January 1':
	print "It's a New year's day!"
elif date == 'July 1':
	print "It's a Canada day!"
elif date == "December 25":
	print "It's a Christmas day!"
else:
	print "There are no fixed-date holidays on that day!"