# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 2016

@author: KevinLiu
"""

# File
xfile = open('mbox.txt')
print xfile

# print mbox
# A text file can be thought of as a sequence of line
for cheese in xfile:
    print cheese
    
# count line of file
count = 0
for line in xfile:
    count = count + 1
print 'Line count: ',count

frand = open('mbox.txt')
inp = frand.read()
print len(inp)
print inp[:20]

# Search through the file
frand = open('mbox.txt')
for line in frand:
    if line.startswith('From:'):
        print line
"""
Outout:
From: rjlowe@iupui.edu

From: wagnermr@iupui.edu

From: david.horwitz@uct.ac.za

each line from the file has a 'newline' notation(/n) at the end
and 'print' add a '/n' auto at the end of printed object
"""

# Fixed
#we can strip the whiteplace from the right-hand side of the string by using 
#rstrip() of the string library
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print line
"""
Outout:
From: rjlowe@iupui.edu
From: wagnermr@iupui.edu
From: david.horwitz@uct.ac.za
"""

# continue
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print line

# select line
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print line

# promote for name
fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened: ',fname
#    exit()
    print 'End'
    
count = 0
for line in fhand:
    if line.startswith('Sbject:'):
        count = count + 1
print 'There were ',count,'subject line in ', fname