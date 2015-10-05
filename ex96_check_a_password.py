# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 96
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 96: Check a Password

def password_checker(password):
	upper = False
	lower = False
	digit = False

	for i in password:
		if i.isupper():
			upper = True
		if i.islower():
			lower = True
		if i.isdigit():
			digit = True

	if upper and lower and digit and len(password)>7:
		return True
	else:
		return False

def main():
	print "Insert password:"
	pswrd = raw_input("> ")
	if password_checker(pswrd):
		print "It's a good password."
	else:
		print "It's not a good password."

if __name__ == "__main__":
	main()