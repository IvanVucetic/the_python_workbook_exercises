# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 123
# Date: 12.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 125: Does a List contain a Sublist?

def isSublist(larger,smaller):
	sub = False
	if smaller == []:
		sub = True
	elif smaller == larger:
		sub = True
	elif len(smaller) > len(larger):
		sub = False
	# go through larger to see if smaller starts at some point	
	else:
		for i in range(len(larger)):
			if larger[i] == smaller[0]:
				n = 1
				# check if subsequent elements are also matching
				while (n < len(smaller)) and (larger[i+n] == smaller[n]):
					n += 1
				# if smaller ended, it is a sublist; if it missmatched earlier- not
				if n == len(smaller):
					sub = True

	return sub

def main(large, small):
	print isSublist(large,small)


a = [1,3,4,5,6]
b = [3,4]

main(a,b)
