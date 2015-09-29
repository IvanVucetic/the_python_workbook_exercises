# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 47
# Date: 29.09.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 47: Birth Date to Astrological Sign

print "Enter your month of birth:"
month = raw_input("> ")
print "Enter your day of birth:"
day = int(raw_input("> "))

if month == 'december':
	sign = 'sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
	sign = 'capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
	sign = 'aquarius' if (day < 19) else 'pisces'
elif month == 'march':
	sign = 'pisces' if (day < 21) else 'aries'
elif month == 'april':
	sign = 'aries' if (day < 20) else 'taurus'
elif month == 'may':
	sign = 'taurus' if (day < 21) else 'gemini'
elif month == 'june':
	sign = 'gemini' if (day < 21) else 'cancer'
elif month == 'july':
	sign = 'cancer' if (day < 23) else 'leo'
elif month == 'august':
	sign = 'leo' if (day < 23) else 'virgo'
elif month == 'september':
	sign = 'virgo' if (day < 23) else 'libra'
elif month == 'october':
	sign = 'libra' if (day < 23) else 'scorpio'
elif month == 'november':
	sign = 'scorpio' if (day < 22) else 'sagittarius'


print sign