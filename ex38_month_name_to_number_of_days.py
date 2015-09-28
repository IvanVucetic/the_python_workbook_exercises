# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 38
# Date: 28.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 38: Month Name to Number of Days

print "Enter a name of the Month:"
month = raw_input("> ")

if month == "February":
	print "28/29 days"
elif month in ("April", "June", "September", "November"):
	print "30 days"
elif month in ("January", "March", "May", "July", "August", "October", "December"):
	print "31 day"
else:
	print "The month doesn't exist"
