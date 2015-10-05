# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 101
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 101: Reduce a Fraction to Lowest Terms

def reduce_fraction(numer, denom):
	#find greatest common divisor
	divisor = numer if numer < denom else denom

	divisor = numer if numer < denom else denom
	while (numer % divisor != 0) or (denom % divisor != 0):
		divisor = divisor - 1
	numer = numer / divisor
	denom = denom / divisor
	return numer, denom

def main():
	print "Insert numerator:"
	n = int(raw_input("> "))
	print "Insert denominator:"
	d = int(raw_input("> "))
	
	print reduce_fraction(n,d)	


main()
