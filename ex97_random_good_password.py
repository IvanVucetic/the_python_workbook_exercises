# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 97
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 97: Random Good Password

from ex94_random_password import password_maker
from ex96_check_a_password import password_checker

def main():
	counter = 0
	while True:
		password = password_maker()
		counter += 1
		if password_checker(password):
			break

	print "Password %s, created in %i attempts." % (password, counter)

main()