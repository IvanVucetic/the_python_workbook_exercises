# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 53
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 53: Assessing Employees

print "Insert a rating of an employee:"
rating = float(raw_input("> "))

if rating == 0:
	meaning = 'unacceptable'
	raise_ = 0
elif rating == 0.4:
	meaning = 'acceptable'
	raise_ = rating * 2400
elif rating == 0.6:
	meaning = 'meritorius'
	raise_ = rating * 2400
else:
	print "Not a valid rating." 
	exit()

print "The performance of the worker is %s and a suggested raise is $%.2f." % (meaning, raise_)

