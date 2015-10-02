# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 79
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 79: Maximum Integer

from random import randint

max = randint(1,100)
print "Initial max is", max
update_count = 0

for i in range(0, 99):
	new_num = randint(1,100)
	if new_num > max:
		max = new_num
		print max, "<== update"
		update_count += 1
	else:
		print new_num

print "The maximum value found is", max
print "The maximum value was updated %i times." % update_count
