# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 11:01:45 2017

@author: ShirleyLiu
"""
# Hash function: Slot ---- item
# The mapping between an item and the slot 
# where that item belongs in the hash table

# Load factor = numberOfItems / tableSize

# Step 1:
# Hash function = “remainder method”  
# (h(item)=item%11h(item)=item%11). 
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos]) #ordinal values

    return sum%tablesize
    
arr = ['c','a','t'] # [2,24,3,8,5]
tablesize = 11

print (hash(arr,tablesize)) #4

# using this function, anagrams will give the same value
# To remedy this: modifications
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + (pos+1) * ord(astring[pos]) #ordinal values

    return sum%tablesize
    
print (hash(arr,tablesize)) #3