#!/usr/bin/env python3

# The For Loop

# i becomes each variable. Four examples.
#This loop retrieves the values of 0 through 26.
#The last value is not included and thus ends on 25.
for i in range(0, 26):    
    print(i)

# Iterate through a range
for i in [1,2,3,4,5,'a','b','c']:
    print(i)
for c in 'password':
    print(c)

#Use of the replacement field {}. to format and print i. 
for i in range(26):
    print("{}".format(i))


for i in range(1,25):
     print("i is now {}".format(i))


