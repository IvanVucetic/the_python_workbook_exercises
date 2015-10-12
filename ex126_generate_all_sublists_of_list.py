# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 123
# Date: 12.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 126: Generate All Sublists of a List

def display_sublists(largelist):
	subs = [[]]
	for i in range(len(largelist)):
		n = i+1
		while n <= len(largelist):
			sub = largelist[i:n]
			subs.append(sub)
			n += 1
	
	return subs

def main():
	a = [1,2,3]
	b = ['a', 'b', 'c']
	print display_sublists(a)
	print display_sublists(b)


main()