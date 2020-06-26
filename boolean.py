#!/usr/bin/env python3

# I may, or may not use this one. But posting it none the-less

#Python does not have boolean data type, but it does have two constants: TRUE and FALSE
#Example: using x as a string. In Python, True is 1 and False is 0.
#But in a condition, any non-zero or non empty values will evaluate to true.

x = "false"
if x:
    print("x is true")
print("""False: {0} 
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string ' ': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False,bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(' '), bool(""), bool({})))

#NOT TRUE = FALSE & FALSE = NOT TRUE
print(not False)
print(not True)
