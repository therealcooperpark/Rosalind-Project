#! /usr/bin/env python3

from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser()
    parser.add_argument('input', help = 'input file')
    return parser.parse_args()


def parse_input(input_file):
    '''
    Parse input file from Rosalind
    '''

    with open(input_file, 'r') as file:
        length = int(file.readline().strip())
        list_to_sort = [int(x) for x in file.readline().strip().split()]
    return length, list_to_sort


def insertion_sort(length, list_to_sort):
    '''
    Run insertion sort on a list
    Keep track of how many swaps happen
    Return sorted list and swap count
    '''

    swap_count = 0

    for idx in range(1, length):
        cur_idx = idx
        while cur_idx > 0 and list_to_sort[cur_idx] < list_to_sort[cur_idx - 1]:
            old, new = list_to_sort[cur_idx], list_to_sort[cur_idx - 1]
            list_to_sort[cur_idx] = new
            list_to_sort[cur_idx - 1] = old
            cur_idx -= 1
            swap_count += 1

    return swap_count, list_to_sort


def main():
    args = get_args()
    length, list_to_sort = parse_input(args.input)
    swap_count, sorted_list = insertion_sort(length, list_to_sort)
    print(swap_count)
#    print(' '.join([str(x) for x in sorted_list]))

if __name__ == "__main__":
    main()
