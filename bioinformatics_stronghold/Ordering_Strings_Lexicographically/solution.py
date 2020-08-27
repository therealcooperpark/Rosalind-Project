#! /usr/bin/env python3

import itertools

# Input values
alphabet = ''.join(input("Enter Lexicographic String:\n").split())
value = int(input("Enter the integer:\n"))


# Create all combinations of string of desired lengths
combinations = []
for number in range(value):
    number += 1

    combs = itertools.product(alphabet, repeat=number)
    for i in combs:
        combinations.append(i)

combinations = sorted(combinations, key = lambda x: [alphabet.index(letter) for letter in x])


with open("Solution.txt", "w") as output:
    for i in combinations:
        output.write('{0}\n'.format("".join(i)))
