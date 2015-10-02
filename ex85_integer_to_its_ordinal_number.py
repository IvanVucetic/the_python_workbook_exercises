# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 85
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 85: Convert an Integer to its Ordinal Number

def ordinal(n):
	if n == 1:
		return 'first'
	elif n == 2:
		return 'second'
	elif n == 3:
		return 'third'
	elif n == 4:
		return 'fourth'
	elif n == 5:
		return 'fifth'
	elif n == 6:
		return 'sixth'
	elif n == 7:
		return 'seventh'
	elif n == 8:
		return 'eighth'
	elif n == 9:
		return 'ninth'
	elif n == 10:
		return 'tenth'
	elif n == 11:
		return 'eleventh'
	elif n == 12:
		return 'twelfth'
	else:
		return ""

if __name__ == '__main__':
	for i in range(1, 13):
		print i, ordinal(i)
else:
	print "imported"
