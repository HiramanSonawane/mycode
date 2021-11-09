#!/usr/bin/env python3

def main():

    mylist= [1,2,3,4,5, "Python"]

    name = input("What is your name?\n" )

    # Hi <name>! Welcome to Day 2 of Python Training!
 #   print("Hi " + name.upper() + "! Welcome to Day " + str(mylist[1]) + " of " + mylist[-1]+  " Training!")
    print(f"Hi { name.upper() }! Welcome to Day {mylist[1]} of {mylist[-1]} Training!")

main()
