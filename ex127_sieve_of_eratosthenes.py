# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 127
# Date: 12.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 127: The Sieve of Eratosthenes

def primes_till_limit(limit):
	# create a list:
	li = []
	for i in range(limit):
		li.append(i)

	# crossing out zero and 1; crossing out = turn to 0
	li[1] = 0

	for i in range(2, len(li)):
		# delete multiples of the number, but not the number itself
		for j in range(i, len(li), i):
			if li[j] != i:
				li[j] = 0

	result = []
	for value in li:
		if value != 0:
			result.append(value)

	return result


print primes_till_limit(100)