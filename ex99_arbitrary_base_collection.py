# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 99
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 99: Arbitrary Base Conversions

# converts a number of a base X to a number of base 10
def convert_2_base_ten(number, base):
	if base not in range(2,17):
		print "Base out of range."
		exit()
	number = list(str(number))	# list, so it could pop()
	decimal = 0

	for i in range(len(number)):
		digit_raw = number.pop() #it might be 0-9, but also A-F; now we check
		if digit_raw.isdigit():
			digit = int(digit_raw)
		else:
			digit_raw = digit_raw.upper()
			digit = ord(digit_raw) - 55
		decimal = decimal + digit*pow(base, i)
	return decimal

# print convert_2_base_ten('1A', 16)

# converts a number of a base 10 to a number of a base base
def convert_from_base_ten(number, base):
	# used algorithm from solutions to exercise 78
	if base not in range(2,17):
		print "Base out of range."
		exit()
	result = ""
	q = number

	r = q % base
	if r < 10:
		result = str(r) + result
	else:
		result = chr(r+55) + result
	q = q // base

	while q > 0:
		r =  q % base
		if r < 10:
			result = str(r) + result
		else:
			result = chr(r+55) + result
		q = q // base

	return result

# print convert_from_base_ten(26, 16)

def main():
	print "Insert a number you wish converted:"
	num = raw_input("> ")
	print "Insert a base in which is your number (2-16):"
	base_from = int(raw_input("> "))
	print "Insert a base of the converted number (2-16):"
	base_to = int(raw_input("> "))

	decimal = convert_2_base_ten(num, base_from)
	result = convert_from_base_ten(decimal, base_to)

	print result

main()