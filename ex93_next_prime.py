# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 93
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 93: Next Prime

def next_prime(n):
	from ex92_is_a_number_prime import is_prime
	next = n+1	# if next = n, it runs is_prime on it and returns it if T
	
	while is_prime(next) is False:
		next += 1
		is_prime(next)
	
	return next

def main():
	print "Insert a number:"
	num = int(raw_input("> "))

	print "The next prime number is", next_prime(num)

main()
