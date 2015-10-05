# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 104
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 104: Sorted Order

lista = []
num = ""
while num != 0:
	try:
		num = int(raw_input("insert number: "))
	except ValueError:
		pass
	lista.append(num)

lista = lista[:-1]
lista.sort()

for i in range(len(lista)):
	print lista[i]

