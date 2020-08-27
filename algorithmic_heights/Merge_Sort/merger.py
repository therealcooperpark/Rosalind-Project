#! /usr/bin/env python3
'''
Merge two sorted lists given
Line 1: Length of line-2 list
Line 2: Sorted list
Line 3: Length of line-4 list
Line 4: Sorted list
'''

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input', help = 'input file from Rosalind')
    parser.add_argument('output', help = 'output file name')
    return parser.parse_args()


def parse_input(input_file):
    '''
    Parse two sorted lists from Rosalind file
    '''

    with open(input_file, 'r') as file:
        next(file)
        list1 = [int(x) for x in file.readline().strip().split()]
        next(file)
        list2 = [int(x) for x in file.readline().strip().split()]

    return list1, list2


def merge_arrays(list1, list2):
    '''
    Merge two sorted lists together
    '''

    merged_list = []
    idx1, idx2 = 0, 0

    # merge the arrays
    while idx1 < len(list1) and idx2 < len(list2):
        # For most of lists, append lowest values at 
        # Each index, increase lowest value idx by 1
        if list1[idx1] < list2[idx2]:
            merged_list.append(str(list1[idx1]))
            idx1 += 1
        else:
            merged_list.append(str(list2[idx2]))
            idx2 += 1
    else:
        # When one list is finished,
        # Append rest of other list to the final list
        print(idx1, len(list1), idx2, len(list2))

        if idx1 == len(list1):
            for idx in list2[idx2:]:
                merged_list.append(str(idx))
        else:
            for idx in list1[idx1:]:
                merged_list.append(str(idx))

    return merged_list


def main():
    args = get_args()
    list1, list2 = parse_input(args.input)
    merged_list = merge_arrays(list1, list2)
    with open(args.output, 'w') as file:
        file.write(' '.join(merged_list))


if __name__ == '__main__':
    main()
