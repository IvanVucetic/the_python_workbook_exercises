# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 135
# Date: 13.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 135: Anagrams

str1 = raw_input("Insert first word: ").lower()
str2 = raw_input("Insert second word: ").lower()

def count(string):
    count = {}
    for s in string:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    return count

if len(str1) != len(str2) or count(str1) != count(str2):
    print "Not anagram!"
else:
    print "Anagram!"


