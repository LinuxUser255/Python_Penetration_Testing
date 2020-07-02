#!/usr/bin/env python3

#Conditions: if else elif.
#A few ways to write them.

#Reading user input 
type = input("Scan type? TCP or UDP: ")
port = int(type("Enter the port number: {0}, ")
       # print("Scanning port {0}, ".format(type))

int = int(input("Enter port number to scan: {0}, ".format(type)))

print(type)

#Using a Replacement field {0}
if age >= 18:
    print("you are old enough to vote")
else:
    print("Return in {0} years".format(18 - age))


age = int(input("your age? "))


#Using () or () 
if (age < 16) or (age > 90):
    print("It's best to call a cab.") 
else:
    print("You can drive.")




#When "and" is used as such: ( ) and  ( ) both statements must be true to satisfy the condition.
#However, when using "or" ( ) or ( ) then only one of the two statements 
#must be true, and must be follwed with an else

