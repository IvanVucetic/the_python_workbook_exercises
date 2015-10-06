# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 110
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 110: Perfect Numbers

def is_perfect_number(n):
	from ex109_list_of_proper_divisors import divisors
	li = divisors(n)
	if sum(li) == n:
		return True
	else:
		return False

def main():
	all_perf = []
	for i in range(1,10001):
		if is_perfect_number(i):
			all_perf.append(i)

	print all_perf

main()