#! /usr/bin/env python3
'''
Find the majority element in a list
'''

import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help = 'input file')
    return parser.parse_args()


def parse_file(input_file):
    '''
    Parse file
    '''

    with open(input_file, 'r') as file:
        threshold = int(file.readline().strip().split()[1]) / 2
        arrays = [ [int(x) for x in line.strip().split()] for line in file.readlines()]
    return threshold, arrays


def find_majority(threshold, array):
    '''
    Find the majority element in given array and 
    minimum threshold
    '''

    counts = {}

    for value in array:
        counts.setdefault(value, 0)
        counts[value] += 1
        if counts[value] > threshold:
            return str(value)
    return '-1'


def main():
    args = get_args()
    threshold, arrays = parse_file(args.input_file)

    majorities = []
    for array in arrays:
        majorities.append(find_majority(threshold, array))
    print(' '.join(majorities))



if __name__ == '__main__':
    main()
