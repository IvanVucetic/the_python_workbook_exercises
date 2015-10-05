# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 105
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 105: Reverse Order

lista = []
num = ""
while num != 0:
	num = int(raw_input("insert number: "))
	lista.append(num)

lista = lista[:-1]
lista.reverse()

for i in range(len(lista)):
	print lista[i]