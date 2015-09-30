# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 64
# Date: 30.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 64: No More Pennies

print "Insert your prices:"

count = 0
sum_ = 0
price = 0

while price != "":
	try:
		price = float(raw_input("> "))
	except ValueError, e:
		break
	sum_ += price
	count += 1

pennies = sum_ % 0.05
print "Total cost: %.2f" % sum_

if pennies < 0.025:
	sum_ -= pennies
else:
	sum_ += 0.05 - pennies

print "Cost for cash: %.2f" % sum_