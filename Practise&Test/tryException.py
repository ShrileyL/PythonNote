# Created by KevinLiu on 16/12/26
# Copyright 2016 KevinLiu. All rights reserved
# 
# Exception 

astr = 'Hello Bob'
try:
	istr = int (astr)
except:
	istr = -1

print 'First', istr

astr = '123'
try:
	istr = int (astr)
except:
	istr = -1

print 'Second', istr


# payment calculator
h = raw_input('Enter Hour: ')
try:
    hour = int(h)
except:
    print 'error, please enter numeric input.'

r = raw_input('Enter Rate: ')
try:
    rate = int(r)
except:
    print 'error, please enter numeric input.'
    
if hour < 40:
    money = hour*rate
else:
    money = 40*rate + (hour-40)*(rate*1.5)

print 'Pay:',money