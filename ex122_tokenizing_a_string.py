# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 122
# Date: 06.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 122: Tokenizing a String

def tokenize(text):
	li = []

	for char in text:
		if char != ' ':
			li.append(char)

	print li
	li_new = [] 

	for i in range(len(li)):
		if li[i] in '+-':
			if (i != 0) and (li[i-1].isdigit() or li[i-1] == ')'): #operator
				li_new.append(li[i])
			else: # part of a number
				n = i + 1
				while li[n].isdigit():
					n += 1
				li_new.append(''.join(li[i:n])) 

		elif li[i].isdigit():
			# i != 0 necessary condition because if both first and last element
			# are digits, it skips the first (because li[-1].isdigit()--> True)
			if i != 0:
				# we want to skip if it's already a part of number
				if li[i-1].isdigit():
					pass
				# previous might be + or - that are part of a number	
				elif li[i-1] in '+-':
					if (i-1 == 0) or (not li[i-2].isdigit() and li[i-2] != ')'):
						pass
					else:
						if i != len(li)-1:
							n = i + 1
							while li[n].isdigit():
								n += 1
							li_new.append(''.join(li[i:n]))
						else:
							li_new.append(li[i])						
				else:
					if i != len(li)-1:
						n = i + 1
						while li[n].isdigit():
							n += 1
						li_new.append(''.join(li[i:n]))
					else:
						li_new.append(li[i])
			else:
				n = i + 1
				while li[n].isdigit():
					n += 1
				li_new.append(''.join(li[i:n]))
		elif li[i] in "*/^()":
		 	li_new.append(li[i])

	print li_new

	


tokenize('+134 - (4 / 2)')

tokenize('16 + 2')







