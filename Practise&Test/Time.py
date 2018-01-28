# # module: time

import time

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:",ticks)

# get UTC time
ticks = time.ctime()
print ("The time is:",ticks)
later = time.time() + 15
print ('15 secs from now :', time.ctime(later))

# find information about "time" module
help(time)

# get current time
localtime = time.localtime(time.time())
print('Current time is: ',localtime)

# convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
localtime = time.asctime(time.localtime(time.time()))
print('Current time is: ',localtime)

# import calendar

# cal = calendar.month(2018,1)
# print("Here is the calender:")
# print(cal)
