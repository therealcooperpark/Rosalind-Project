#! /usr/bin/env python3
'''
Calculate all combinations given the sample size and number of items
'''

from scipy.special import comb


def main():
    N = int(input("Enter N:\n"))
    M = int(input("Enter M:\n"))

    total_combs = 0
    for rng in range(M, N + 1):
        total_combs += comb(N, rng, exact = True)

    print( total_combs % 1000000 )

if __name__ == "__main__":
    main()
