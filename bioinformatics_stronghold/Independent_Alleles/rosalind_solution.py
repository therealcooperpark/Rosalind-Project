#! /usr/bin/env python3

from scipy.stats import binom

k = 2 ** int(input("Enter k:\n"))
n = int(input("Enter N:\n"))

print(1 - binom.cdf(n-1, k, 0.25) )
