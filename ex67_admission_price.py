# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 67
# Date: 30.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 67: Admission Price

sum_ = 0
age = 0

while age != "":
	try:
		age = int(raw_input("> "))
	except ValueError:
		break

	if age <= 2:
		pass
	elif 2 < age <= 12:
		sum_ += 14
	elif age >= 65:
		sum_ += 18
	else:
		sum_ += 23

print "Price of a group ticket is $%.2f" % sum_