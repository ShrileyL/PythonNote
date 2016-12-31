# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:05:07 2016

@author: KevinLiu
"""

# the element in the list can be any Python object
l = [1,'ede',3.1212,[7,3,2]]

for i in l:
    print i
print 'Done'

# index of the list
print l[1]
# start from zero

# strings are immutable
# while lists are mutable
fruit = 'Banana'
#fruit[0] = 'b'
x = fruit.lower()
print x

lotter = [3,8,23,45,73,22]
lotter[2] = 28
print lotter

# range() function
#return a list of member begin fron zero to less than the paramenter
range(4)
print len(lotter)
print range(len(lotter))

for i in range(len(lotter)):
    print 'Number:',lotter[i]

# sliced: link string,the second number is "Upto but not include"
print lotter[1:3]

# list method
x = list()
type(x)
dir(x)
x.append(1)
x.append(22)
x.append(7)
x.append(13)
print x
x.sort()
print x

# string and list
# default split use 'space'
line = 'A lot    of space'
thing = line.split()
print thing

line = 'first;second;third'
thing = line.split()
print thing
# use ';' to split
thing = line.split(';')
print thing

# costomise split
line = 'he.ss.dada'
thing = line.split('.')
print thing