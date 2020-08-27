#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    return parser.parse_args()


def parse_input(input_file):
    '''
    Open input file, return list and k
    '''

    with open(input_file, 'r') as file:
        next(file)
        array = [int(x) for x in file.readline().strip().split()]
    return array


def quick_sort(array):
    '''
    Find the k-th lowest value in an unsorted array
    '''

    if array == []: # Base case
        return array


    split_value = array[len(array)//2] # Randomly take split_value
    lower, mid, upper = split_array(array, split_value) # Split on value
    return quick_sort(lower) + mid + quick_sort(upper) # Sort each portion and return



def split_array(array, split_value):
    '''
    Split array into three parts using
    given split_value
    '''

    lower, mid, upper = [], [], []
    for num in array:
        if num < split_value:
            lower.append(num)
        elif num == split_value:
            mid.append(num)
        else:
            upper.append(num)
    return lower, mid, upper


def main():
    args = get_args()
    array = parse_input(args.input_file)
    sorted_array = quick_sort(array)
    with open(args.output_file, 'w') as file:
        out = [str(x) for x in sorted_array]
        file.write(' '.join(out))


if __name__ == '__main__':
    main()
