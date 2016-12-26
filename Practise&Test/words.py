# Created by KevinLiu on 16/12/23.
# Copyright © 2016年 KevinLiu. All rights reserved.
# Target: count for frequences of word

# Get the name of the file and open it
name = raw_input('Enter file:')
handle = open(name, 'r')
text = handle.read()
words = text.split()

# count word frequency
counts = dict()
for word in words: 
    counts[word] = counts.get(word,0) + 1

# Find the most common word
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount == None or count > bigcount:
        bigword = word 
        bigcount = count 

# All done
print bigword, bigcount

# type()
x = 12
message = 'we'

type(x)
type(message)


# Type conversion
prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
speed = raw_input(prompt)
print int(speed) + 1