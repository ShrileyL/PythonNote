# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 09:51:27 2017

@author: ShirleyLiu

Purposes: This codes just be used to help understand algorithms,
        to show algorithms use simply codes
"""

#Select Sort
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    
def SelectSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
    
print(SelectSort([5,3,6,2,10]))
#print SelectSort([5,3,6,2,10])

#Quick Sort
def QuickSort(arr):
    if len(arr) < 2:
        return arr #base condition
    else:
        pivot = arr[0] #default pivot
        less = [i for i in arr[1:] if i <= pivot]
        larger = [i for i in arr[1:] if i > pivot]
        return QuickSort(less) + [pivot] + QuickSort(larger)
        
print(QuickSort([10,5,3,2]))

#Buble Sort
def BubbleSort(arr):
    for passnum in range(len(arr)-1, 0, -1):
        for i in range(passnum):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    
alist = [54,26,93,17,77,31,44,55,20]
BubbleSort(alist)
print(alist)

#Merge Sort
def MergeSort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    MergeSort(lefthalf)
    MergeSort(righthalf)

    # merge two half into orignal arr
    i = j = k = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            arr[k] = lefthalf[i]
            i = i + 1
        else:
            arr[k] = righthalf[j]
            j = j + 1
        k = k + 1

    while i < len(lefthalf):
        arr[k] = lefthalf[i]
        i = i + 1
        k = k + 1

    while j < len(righthalf):
        arr[k] = righthalf[j]
        j = j + 1
        k = k + 1


alist = [54,26,93,17,77,31,44,55,20]
MergeSort(alist)
print(alist)