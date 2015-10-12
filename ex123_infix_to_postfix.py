# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 123
# Date: 07.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 123: Infix to Postfix

def infix2postfix(infix):
	from ex90_does_a_string_represent_an_integer import is_integer
	from ex91_operator_precedence import precedence

	operators = []
	postfix = []

	for token in infix:
		if token.isdigit(): # ! ex.90---> program bad, recognizes + and - as int
			postfix.append(token)
		if token in "*/+-^": 
			while (len(operators) > 0) and (operators[-1] != '(') and \
				(precedence(token) < precedence(operators[-1])): # ex.91
				postfix.append(operators.pop())
			operators.append(token)
		if token == "(":
			operators.append(token)
		if token == ")":
			while operators[-1] != "(":
				postfix.append(operators.pop())
			operators = operators[:-1]

	while len(operators) > 0:
		postfix.append(operators.pop())

	return postfix


def main():
	from ex122_tokenizing_a_string import tokenize

	exp = raw_input("Insert an expression: ")
	li = tokenize(exp)

	print infix2postfix(li)

main()