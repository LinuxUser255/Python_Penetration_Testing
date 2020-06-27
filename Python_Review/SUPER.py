#!/usr/bin/env python3

#Recursion Super Power
def move(f,t):

   print("Move disc from {} to {}!".format(f,t))

#Easy case for Hanoi
def hanoi(n,f,h,t) :
    if n == 0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)
    hanoi(4,"A","B","C")
