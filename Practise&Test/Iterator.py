# Created by KevinLiu on 16/12/27
# Copyright 2016 KevinLiu. All rights reserved
# 
# Loops and iterator

# Demo of 'break'
while True:
    line = raw_input('> ')
    if line == 'Done' or line == 'done':
        break
    print line
print 'Done'

# use 'continue' to break
while True:
    line = raw_input('> ')
    if line[0] == '#':
        continue
    if line == 'Done' or line == 'done':
        break
    print line
print 'Done!'

# a definite loop in string
friends = ['Kevin','Lucy','Shirley','Jack']
for friend in friends:
    print 'Happy New Year! ',friend
print 'Done!'

# Find the Largest number
largest_so_far = -1
print 'Before ',largest_so_far
for i in [3,12,45,17,9,28]:
    if largest_so_far <= i:
        largest_so_far = i
    print largest_so_far, i

print 'After ',largest_so_far