#! /usr/bin/env python3

string = input("Enter string:\n")

nucs = {}
for nuc in string:
    nucs.setdefault(nuc, 0)
    nucs[nuc] += 1

print(nucs)
