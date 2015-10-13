# Exercises from the book:
# Ben Stephenson - The Python Workbook
#
# Exercise no. 136
# Date: 13.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 136: Anagrams Again

def count(string):
    count = {}
    for s in string:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    return count

str1 = raw_input("Insert first word: ").lower()
str2 = raw_input("Insert second word: ").lower()

# join words
str1 = "".join(str1.split())
str2 = "".join(str2.split())
# exclude punctuation marks
str1 = str1.translate(None, ",.!?")
str2 = str2.translate(None, ",.!?")

if len(str1) != len(str2) or count(str1) != count(str2):
    print "Not anagram!"
else:
    print "Anagram!"
