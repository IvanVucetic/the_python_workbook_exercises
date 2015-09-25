# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 12
# Date: 25.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 12: Distance Between Two Points on Earth

from math import radians, sin, cos, acos

print "This program calculates the distance between points on Earth."
print "Insert coordinates of your points:"
print ""
lat1 = radians(float(raw_input("latitude 1: ")))
lon1 = radians(float(raw_input("longitude 1: ")))
lat2 = radians(float(raw_input("latitude 2: ")))
lon2 = radians(float(raw_input("longitude 2: ")))

print lat1, lat2, lon1, lon2

dist = 6371.01 * acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(lon1 - lon2))
print "The distance is %.2fkm." % dist
