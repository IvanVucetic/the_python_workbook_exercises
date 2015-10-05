# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 94
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 94: Random Password

def password_maker():
	from random import randint

	password = ""
	for i in range(randint(7,10)):
		password = password + chr(randint(33,126))

	return password

def main():
	print password_maker()

if __name__ == "__main__":
	main()