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

inp = xfile.read()
print len(inp)