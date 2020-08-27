#! /usr/bin/env python3

import itertools

num = int(input("Enter number of values for permutations:\n"))
values = []
for i in range(num):
    values.append(-i - 1)
    values.append(i + 1)

perms = []
# All permutations of the collection
for perm in itertools.permutations(values, num):
    if len(set(map(abs, perm))) == num:
        perms.append(list(perm))


with open("answer.txt", "w") as output:
    output.write("{0}\n".format(len(perms)))
    for perm in perms:
        out = list(map(str, perm))
        output.write("{0}\n".format(" ".join(out)))
