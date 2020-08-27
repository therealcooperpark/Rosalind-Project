#! /usr/bin/env python3

import argparse
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("first", type = int)
parser.add_argument("second", type = int)
args = parser.parse_args()

perms = []
for i in range(args.first):
    perms.append(i)

total = len(list(itertools.permutations(perms, args.second)))

print(total % 1000000)


