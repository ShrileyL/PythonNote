# Created by KevinLiu on 16/12/27
# Copyright 2016 KevinLiu. All rights reserved
# 
# String

# for string, + means 'concatenate'
str1 = "Hello"
str2 = 'World'
str3 = str1 + str2
print str3

# index value start from 0
letter = str1[1]
print letter

# string lenth
print len(str1)

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print index,letter
    index = index + 1
    
# slicing string
s = 'Hello Python'
# do not include right side
print s[:6]
print s[:7]
# include left side
print s[3:]

# converse to lower letter
print s.lower()

# converse to upper letter
print s.upper()

# string library
dir(s)