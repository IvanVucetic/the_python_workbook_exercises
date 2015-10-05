# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 102
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 102: Reduce Measures

def reduce_measures(number, unit):
	unit = unit.lower() # to enable for upper and lower case

	# initial values; if not assigned and aren't any, error (ref before assign) 
	cups = 0
	tabspoons = 0
	teaspoons = 0

	if unit == "cup" or unit == "cups":
		cups = number
	elif unit == "tablespoon" or unit == "tablespoons":
		cups = number // 16
		tabspoons = number - cups*16
	else:
		cups = number // 48
		tabspoons = (number - cups*16) // 3
		teaspoons = number - cups*16 - tabspoons*3

	result = ""

	if cups > 0:
		result = result + str(cups) + " cup"
		if cups > 1:
			result = result + "s"
	
	if tabspoons > 0:
		if result != "":
			result = result + ", "
		result = result + str(tabspoons) + " tablespoon"
		if tabspoons > 1:
			result = result + "s"
	
	if teaspoons > 0:
		if result != "":
			result += ", "
		result = result + str(teaspoons) + " teaspoon"
		if teaspoons > 1:
			result += "s"

	if result == "":
		result = "0 teaspoons"

	return result

print reduce_measures(65, "teaspoons")
