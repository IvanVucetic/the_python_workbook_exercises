# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 92
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 92: Is a Number Prime?

def is_prime(num):
	prime = True
	if num < 1:
		print "Not a valid number."
	else:
		for i in range(2, num):
			if num % i == 0:
				prime = False
		return prime

def main():
	print "Insert a number:"
	try:
		number = int(raw_input("> "))
	except ValueError:
		print "Not a number."
		exit()
	

	if is_prime(number):
		print "It is a prime number."
	else:
		print "It is NOT a prime number."


if __name__ == "__main__":
	main()