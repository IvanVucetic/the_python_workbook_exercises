# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 70
# Date: 30.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 70: Caesar Cipher

lower = []
upper = []

for i in range(97, 123):
	lower.append(chr(i))
for i in range(65, 91):
	upper.append(chr(i))

print "Insert your message:"
message = raw_input("> ")
print "Insert shift:"
shift = int(raw_input("> "))

cip_letters = []

for letter in message:
	if letter in upper:
		position = upper.index(letter)
	elif letter in lower:
		position = lower.index(letter)
	else:
		pass

	new_pos = (position + shift) % 26
	
	if letter in upper:
		new_letter = upper[new_pos]
	elif letter in lower:
		new_letter = lower[new_pos]
	else:
		new_letter = letter
	cip_letters.append(new_letter)

cip_message = ''.join(cip_letters)
print cip_message