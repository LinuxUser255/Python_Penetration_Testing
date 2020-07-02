#!/usr/bin/env python3

#Recursion
# A Recursion function calls on itself
#And works simialr to a loop
def rec_fun(k):
  if(k > 0):
    result = k + rec_fun(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nThis is what recursion looks like")
rec_fun(4)
