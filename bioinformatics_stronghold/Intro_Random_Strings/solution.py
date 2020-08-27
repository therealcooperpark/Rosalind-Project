#! /usr/bin/env python3

import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--string", help = "DNA String")
parser.add_argument("-v", "--values", type = float, nargs = "*", help = "List of log values to match")
args = parser.parse_args()

solution = []

for n in args.values:
    string_prob = 1
    AT = (1-n)/2
    GC = n/2

    for i in args.string:
        if i == "A" or i == "T":
            string_prob *= AT
        else:
            string_prob *= GC

    solution.append(float("{0:.3f}".format(math.log10(string_prob))))

print(solution)

