# Ben Stephenson - The Python Workbook
#
# Exercise no. 148
# Date: 19.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 148: Sum a List of Numbers

print "Enter a number:"
num = raw_input("> ")
sum_ = 0

while num != "":
	try:
		sum_ += float(num)
	except ValueError:
		pass

	print "Current sum:", sum_
	print "Enter a number (blank to finish):"
	num = raw_input("> ")

print "Final sum:", sum_