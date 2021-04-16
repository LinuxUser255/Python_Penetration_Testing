#!/usr/bin/env python3

# how to use a variable inside a string
# the {} {} double brackets hold the variables
# and the f" " formats the string,
# place an f before the "" to insert a vars value into a string

first_name = "peter"
last_name = "gibbons"

full_name = f"{first_name} {last_name}"
print(full_name)

print(60*"-")

city = "tampa"
state = "florida"
country = "united states"
space = "\n\t"

location = f"{space} {state} {country}"
print(location.title())
