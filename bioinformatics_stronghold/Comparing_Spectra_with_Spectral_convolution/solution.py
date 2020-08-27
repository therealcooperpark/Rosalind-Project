#! /usr/bin/env python3
'''
Solution for Comparing Spectra with Spectral Convolution challenge from Rosalind Project
'''


def parse_multisets(dataset):
    '''
    Parse the two line data file into two float based lists
    '''

    with open(dataset, "r") as file:
        multiset1 = [float(x) for x in file.readline().split()]
        multiset2 = [float(x) for x in file.readline().split()]
    return multiset1, multiset2


def minkowski_dif(m1, m2):
    '''
    Return a multiset of the absolute value of all minkowski_dif of m1 - m2 pairs
    '''

    min_multiset = []
    for x in m1:
        for y in m2:
            min_multiset.append(round(abs(x - y), 5))
    return min_multiset


def max_multiplicity(multiset):
    '''
    Return the value with the largest multiplicity from a given list
    '''

    multiplicity = {}
    max_multi = (None, 0)
    for value in multiset:
        multiplicity.setdefault(value, 0)
        multiplicity[value] += 1
        if max_multi[1] < multiplicity[value]:
            max_multi = (value, multiplicity[value])
    return max_multi


def main():
    dataset = input("Enter filepath to dataset file:\n")
    multiset1, multiset2 = parse_multisets(dataset)
    spec_convolution = minkowski_dif(multiset1, multiset2)
    print(spec_convolution)
    multi_value = max_multiplicity(spec_convolution)
    print(multi_value[1])
    print(multi_value[0])


if __name__ == "__main__":
    main()
