#!/usr/bin/env python3

#Conditions: if else elif.
#A few ways to write them.

#Reading user input 
name = input("enter name: ")
age = int(input("how old are you, {0}? ".format(name)))
print(age)

#Using a Replacement field {0}
if age >= 18:
    print("you are old enough to vote")
else:
    print("Return in {0} years".format(18 - age))


age = int(input("your age? "))

#Using () and ()
if (age == 16) and (age == 16):
    print("have fun")
else:
    print("get to work")

#Using () or () 
if (age < 16) or (age > 65):
    print("enjoy it while it lasts") 
else:
    print("have a good day at work")



#When "and" is used as such: ( ) and  ( ) both statements must be true to satisfy the condition.
#However, when using "or" ( ) or ( ) then only one of the two statements 
#must be true, and must be follwed with an else

