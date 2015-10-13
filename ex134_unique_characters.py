# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 134
# Date: 13.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 134: Unique Characters

from sets import Set
string = raw_input("Insert text: ")
unique = Set([])

for char in string:
	if char in unique:
		pass
	else:
		unique.add(char)

print "Number of unique characters:", len(unique)


# using dictionary:
# if char in dict.keys():
# 	pass
# else:
# 	dict[char] = 1

# print len(dict)