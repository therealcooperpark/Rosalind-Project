#! /usr/bin/env python3
'''
Calculate the probability that two diploid siblings
share at least k of their 2n chrmsm
'''

import math

def binomial(chrmsm, matches):
    # Calculates binomial probability of 'matches' occuring over 'chrmsm'
    combinations = math.factorial(chrmsm) / math.factorial(matches) / math.factorial(chrmsm - matches)
    return combinations * (.5**chrmsm)

def write_output(prob_list):
    # Write out list on single line
    with open("answer.txt", "w") as output:
        output.write(" ".join(prob_list))


def main():
    n = int(input("Enter n:\n"))

    prob_list = []
    for event in range(2*n, -1, -1):
        prob_list.append(binomial(n*2, event))
    prob_list = [math.log10(sum(prob_list[:i])) for i in range(2*n, 0, -1)]

    prob_list = [str(x) for x in prob_list]
    write_output(prob_list)


if __name__ == "__main__":
    main()
# Probability of 0 is probability of 1 + prob(2) + prob(3)...
