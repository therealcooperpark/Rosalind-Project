#! /usr/bin/env python3
'''
Perform binary search
'''

import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help = 'file for script')
    return parser.parse_args()


def binary_search(reference, left, right, query):
    '''
    Perform binary search.
    Return -1 if not found.
    '''

    # Base case
    if right >= left:

        # Get mid
        mid = left + (right - left) // 2

        # If equal, return idx
        if reference[mid] == query:
            return str(mid+1)

        # If greater than query, shift frame to lower half of frame
        elif reference[mid] > query:
            return binary_search(reference, left, mid-1, query)

        # If lower than query, shift frame to upper half of frame
        elif reference[mid] < query:
            return binary_search(reference, mid+1, right, query)

    else:
        # If empty, return base case
        return '-1'


def main():
    args = get_args()
    with open(args.input_file, 'r') as file:
        next(file)
        next(file)
        reference = [int(x) for x in file.readline().strip().split()]
        queries = [int(x) for x in file.readline().strip().split()]

    results = []
    print(reference, '\n', queries)
    for num in queries:
        pos = binary_search(reference, 0, len(reference)-1, num)
        results.append(pos)
    with open('answer.txt', 'w') as file:
        file.write(' '.join(results))

if __name__ == "__main__":
    main()
