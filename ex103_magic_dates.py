# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 103
# Date: 05.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 103: Magic Dates

def magic_date(day, month, year):
	if (day * month) % 100 == year % 100:
		return True
	else:
		return False

def main():
	from ex100_days_in_a_month import days_in_month

	
	for year in range(1900, 2001):
		for month in range(1,13):
			for day in range(days_in_month(month, year) + 1):
				if magic_date(day, month, year):
					print day, month, year

main()

# for some reason, main() from ex100 runs even though it shouldn't!!!