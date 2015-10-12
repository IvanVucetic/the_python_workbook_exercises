# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 123
# Date: 12.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 124: Evaluate Postfix

def evaluate_postfix(post):
	values = []
	for token in post:
		if token.isdigit():
			values.append(int(token))
		else:
			right = values.pop()
			left = values.pop()
			if token == '+':
				val = left + right
			elif token == '-':
				val = left - right
			elif token == '/':
				val = left / right
			elif token == '*':
				val = left * right
			else:
				val = left**right
			values.append(val)

	return values[0]

def main():
	from ex122_tokenizing_a_string import tokenize
	from ex123_infix_to_postfix import infix2postfix

	exp = raw_input("Insert expression: ")
	inf = tokenize(exp)
	postf = infix2postfix(inf)

	print evaluate_postfix(postf)

if __name__ == "__main__":
	main()