# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 76
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 76: Prime Factors

print "Insert number to get its prime factorials:"

n = True
while n < 2:
	n = int(raw_input("> "))
	print "Number must be greater than 2. Try again"

fact = 2

while fact <= n:
	if n % fact == 0:
		print fact
		n = n / fact
	else:
		fact += 1