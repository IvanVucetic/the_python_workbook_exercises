# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 106
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 106: Remove Outliers

def outliers(li,n):
	if len(li) < 2*n:
		print "Not enough elements."
		exit()
	li.sort()
	li1 = li[n:-n]
	return li1


def main():
	li = []
	element = 0
	while element != "":
		try:
			element = int(raw_input("> "))
		except ValueError:
			break
		li.append(element)
	li = li[:-1]
	
	print outliers(li, 2)
	print li

main()

