# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 121
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 121: Count the Elements

def count_range(li, min, max):
	counter = 0
	for el in li:
		if min <= el <= max:
			counter += 1
	return counter

def main():
	list1 = [1,2,3,5,5,5,7,8,9999]
	print count_range(list1, 3, 100)

	list2 = ['a','b','c','d']
	print count_range(list2, 'b', 'z')


main()