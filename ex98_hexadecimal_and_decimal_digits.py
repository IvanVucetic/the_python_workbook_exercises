# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 98
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 98: Hexadecimal and Decimal Digits

def hex2int(hex_):
	if len(hex_)>1:
		decimal = "Can convert a single character only"
		return decimal
	if hex_.isdigit():
		decimal = hex_
	else:
		hex_ = hex_.upper()
		if 65 <= ord(hex_) <= 70:
			decimal = ord(hex_) - 55
		else: 
			decimal = "Not a valid Hexadecimal symbol"
	return decimal

def int2hex(dec):
	if dec > 15:
		print "Only converts numbers 0-15"
		exit()
	if dec < 10:
		hex_ = dec
	else:
		hex_ = chr(dec + 55)
	return hex_

print hex2int('9')
print hex2int('!')
print hex2int('asd')
print int2hex(13)
print int2hex(17)