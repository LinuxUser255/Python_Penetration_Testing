#!/usr/bin/env python3

answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input())

#Round 1
if guess < answer:
     print("Please guess higher, R1")
     guess = int(input())
     if guess == answer:
         print("Well done, you guessed it, R1")
     else:
         print("Sorry, you have not guessed correctly R1")
elif guess > answer:
     print("Please guess lower, R1")
     guess = int(input())
     if guess == answer:
         print("Well done, you guessed it, R1")
     else:
        print("Sorry, you have not guessed correctly, R1")
else:
    print("1 You got it first time, R1")


#Round 2
if guess < answer:
     print("Please guess higher, R2")
     guess = int(input())
     if guess == answer:
         print("Well done, you guessed it, R2")
     else:
         print("Sorry, you have not guessed correctly, R2")
elif guess > answer:
     print("Please guess lower, R2")
     guess = int(input())
     if guess == answer:
         print("Well done, you guessed it, R2")
     else:
        print("Sorry, you have not guessed correctly, R2")
else:
    print("first try ,R2")


#Round 3
if guess < answer:
     print("Please guess higher, R3")
     guess = int(input())
     if guess == answer:
         print("Well done, you guessed it, R3")
     else:
         print("Sorry, you have not guessed correctly, R3")
elif guess > answer:
     print("Please guess lower, R3")
     guess = int(input())
     if guess == answer:
         print("Well done, you guessed it, R3")
     else:
        print("Sorry, you have not guessed correctly, R3")
else:
    print("first try ,R3")


#Round 4
if guess < answer:
     print("Please guess higher, R4")
     guess = int(input())
     if guess == answer:
         print("Well done, you guessed it, R4")
     else:
         print("Sorry, you have not guessed correctly, R4")
elif guess > answer:
     print("Please guess lower, R4")
     guess = int(input())
     if guess == answer:
         print("Well done, you guessed it, R4")
     else:
        print("Sorry, you have not guessed correctly, R4")
else:
    print("first try ,R4")



