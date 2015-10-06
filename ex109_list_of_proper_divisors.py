# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 109
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 109: List of Proper Divisors

def divisors(n):
	li = []
	for k in range(1,n):
		if n % k == 0:
			li.append(k)

	return li

def main():
	print "Insert an integer whose divisors you want:"
	val = int(raw_input("> "))
	print "Divisors of %i are:" % val
	print divisors(val)

if __name__ == "__main__":
	main()
