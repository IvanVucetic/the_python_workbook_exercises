# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 120
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 120: Is a List already in Sorted Order?

def is_sorted(list_):
	return list_ == sorted(list_)

def main():
	li = []
	x = raw_input("Insert a list, element by element (blank to stop):")
	while x != "":
		li.append(float(x))
		x = raw_input("Insert a list, element by element (blank to stop):")

	if is_sorted(li):
		print "The list is sorted."
	else:
		print "The list is NOT sorted."

main()
