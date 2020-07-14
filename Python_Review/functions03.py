#!/usr/bin/env python3

def get_formatted_name(first_name, last_name):

    full_name = f"{first_name} {last_name}"
    return full_name.title()


#While loop
while True:
    print ("\nPlease tell me your name ")
    f_name = input("first name: ")
    l_name = input("Last Name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHi, {formatted_name}!")
    break

