# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:53:56 2016

@author: KevinLiu
"""

purse = dict()
purse['clothes'] = 2
purse['fruit'] = 12
purse['vegetables'] = 24
print purse

# use dict to count
count = dict()
names = ['csve','seve','jackie','seve','jackie','seve']
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1
print count

count = dict()
names = ['csve','seve','jackie','seve','jackie','seve']
for name in names:
    count[name] = count.get(name,0) + 1
print count

# counting pattern
counts = dict()
print 'Enter a line of text:'
line = raw_input(' ')
words = line.split()
print words

for word in words:
    counts[word] = counts.get(word,0) + 1
print 'Counting: '
print counts