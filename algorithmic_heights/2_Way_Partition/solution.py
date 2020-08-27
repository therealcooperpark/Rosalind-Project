#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    return parser.parse_args()


def parse_input(input_file):
    '''
    Parse input list from file
    '''

    with open(input_file, 'r') as file:
        next(file)
        input_list = [int(x) for x in file.readline().strip().split()]
    return input_list


def permute_sort_list(input_list):
    '''
    Sort the list so that values less than
    input_list[0] are on left, and values
    larger on the right
    '''

    target_value = input_list[0]
    permuted_list = []

    for value in input_list:
        if value <= target_value:
            permuted_list.insert(0, value)
        else:
            permuted_list.append(value)

    return permuted_list


def write_output(permuted_list, output_file):
    '''
    Write list to output_file
    '''

    with open(output_file, 'w') as file:
        out_list = [str(x) for x in permuted_list]
        file.write(' '.join(out_list))


def main():
    args = get_args()
    input_list = parse_input(args.input_file)
    permuted_list = permute_sort_list(input_list)
    write_output(permuted_list, args.output_file)


if __name__ == '__main__':
    main()
