# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 113
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 113: Formatting a List

def list_2_string(li):
	if len(li) == 1:
		print li[0]
	elif len(li) == 2:
		print "%s and %s" % (li[0], li[1])
	else:
		for e in range(len(li)-2):
			print "%s," % li[e],
		print "%s and" % li[-2],
		print li[-1]

def main():
	li = []
	item = raw_input("Enter an item: ")
	while item != "":
		li.append(item)
		item = raw_input("Enter an item: ")
	list_2_string(li)

main()

		