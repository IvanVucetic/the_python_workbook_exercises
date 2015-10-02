# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 78
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 78: Decimal to Binary

from math import log, pow

print "Insert an integer to get a binary representation:"
decimal = int(raw_input("> "))
positions = []

# to get positions on which 1 should be:
while decimal > 0:
	power = int(log(decimal, 2)) # e.g. dec = 5 ==> pow = 2; pow(2,2) = 4
	positions.append(power)
	decimal = decimal - pow(2, power)

# insert 1 into those positions
bin_list = []
for i in range(max(positions) + 1):
	if i in positions:
		bin_list.append('1')
	else:
		bin_list.append('0')

# position 0 is first in a list, but should be last when writing number
bin_list.reverse()
print "The binary number is", "".join(bin_list)

# Solved the exercise my way, before looking at the algorithm provided by 
# the Author. Compared 2 solutions afterward and found Author's to be
# much simpler and easier.