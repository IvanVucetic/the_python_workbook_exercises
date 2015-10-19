# Ben Stephenson - The Python Workbook
#
# Exercise no. 147
# Date: 19.10.2015
#
# Ivan Vucetic
# vuceta87@yahoo.com


# Exercise 147: Words that Occur Most

from ex111_only_the_words import split_2_words

filename = raw_input("The file you want to analyze: ")
txt = open(filename, 'r')

d = {}

for line in txt.readlines():
	line = split_2_words(line)
	# now go word by word in a line
	for word in line:
		word = word.lower()
		if word in d.keys():
			d[word] += 1
		else:
			d[word] = 1
# print d

m = max(d.values())
common = []
for word in d:
	if d[word] == m:
		common.append(word)

print "The most common word(s):", common	
