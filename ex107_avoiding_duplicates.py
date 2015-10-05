# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 107
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 107: Avoiding Duplicates

li = []

print "Insert words:"

el = raw_input("> ")
li.append(el)

while el != "":
	el = raw_input("> ")
	if el not in li:
		li.append(el)

li = li[:-1]

for el in li:
	print el 