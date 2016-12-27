# Created by KevinLiu on 16/12/26
# Copyright 2016 KevinLiu. All rights reserved
# 
# Function

def fun():
    print 'Hello,Function'

# definine the computePay function
def computePay(_hour, _rate):
    try:
        hour = int(_hour)
    except:
        return 'error, please enter numeric input.'
	
    try:
        rate = int(_rate)
    except:
        return 'error, please enter numeric input.'
    
    if hour < 40:
        money = hour*rate
    else:
        money = 40*rate + (hour-40)*(rate*1.5)

    return money

print computePay(45,10)

###################################################
# random
import random

for i in range(10):
    x = random.random()
    print x

print 'end'

# randint(low,high)
# return int between low and high (include both sides)
random.randint(1 ,10)

# to choose element from a sequense at random
t = [2,1,3,56,7]
random.choice(t)

###################################################
# math
import math
print math

radient = 0.7
height = math.sin(radient)
print height

ratio = 100
print math.log10(ratio)