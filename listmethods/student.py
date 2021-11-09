#!/usr/bin/env python3

icecream= ["indentation", "spaces"]

northerntrust= ["Darrin","Hiraman","Marc","Michael","Prarthana","Shrikant"]

icecream.append(4)

print(icecream)
print(northerntrust)

student_index=int(input("Enter the Student index [0-4]: "))
student=northerntrust[student_index]

print(f"{student} always uses {icecream[-1]} <spaces> to indent.")
