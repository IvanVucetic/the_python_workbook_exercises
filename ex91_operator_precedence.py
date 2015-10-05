# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 91
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 91: Operator Precedence

def precedence(string):
	if string in "+-":
		return 1
	elif string in "*/":
		return 2
	elif string == "^":
		return 3
	else:
		return -1

def main():
	print "Insert an operator:"
	oper = raw_input("> ")

	if len(oper) != 1 or precedence(oper) == -1:
		print "Not a valid operator."
	else:
		print precedence(oper)

if __name__ == '__main__':
	main() 