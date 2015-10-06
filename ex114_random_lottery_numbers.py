# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 114
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 114: Random Lottery Numbers

from random import randint

numbers = []
num = randint(1,49)

while len(numbers) < 6:
	if num not in numbers:
		numbers.append(num)
	num = randint(1,49)

numbers.sort()
print numbers