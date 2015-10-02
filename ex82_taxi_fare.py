# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 82
# Date: 02.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 82: Taxi Fare

def fare_price(distance):
	base_fare = 4
	fare = (distance / 0.14) * 0.25
	total_fare = base_fare + fare

	print "Total fare is %.2f dollars." % total_fare

print "Insert distance in kilometers:"
dist = float(raw_input("> "))

fare_price(dist)