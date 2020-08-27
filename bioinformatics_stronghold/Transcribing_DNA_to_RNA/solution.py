#! /usr/bin/env python3

string = input("Enter string:\n")

with open("output.txt", "w") as output:
    output.write(string.replace("T", "U"))
