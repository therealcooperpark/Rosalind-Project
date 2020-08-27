#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    return parser.parse_args()


def parse_input(input_file):
    '''
    Open input file, return list and k
    '''

    with open(input_file, 'r') as file:
        next(file)
        array = [int(x) for x in file.readline().strip().split()]
        k = int(file.readline().strip())
    return array, k


def find_median(array, k):
    '''
    Find the k-th lowest value in an unsorted array
    '''

    split_value = array[len(array)//2]
    lower, mid, upper = split_array(array, split_value)
    print(lower, '\n', mid, '\n', upper)
    print('----------')
    if k <= len(lower):
        return find_median(lower, k)
    elif len(lower) < k and k <= len(lower) + len(mid):
        return mid[0]
    else:
        return find_median(upper, k - (len(lower) + len(mid)))


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
    array, k = parse_input(args.input_file)
    median = find_median(array, k)
    print(median)


if __name__ == '__main__':
    main()
