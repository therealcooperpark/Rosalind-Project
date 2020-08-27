#! /usr/bin/env python3
'''
Do Merge Sort
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
        list_to_sort = [int(x) for x in file.readline().strip().split()]
    return list_to_sort


def merge_sort(list_to_sort, iter):
    '''
    Recursively Merge arrays
    '''
    print(list_to_sort, iter)

    if len(list_to_sort) == 1:
        return list_to_sort

    midpoint = len(list_to_sort) // 2
    listA = list_to_sort[:midpoint]
    listB = list_to_sort[midpoint:]

    if len(listA) >= 2:
        listA = merge_sort(listA, iter + 1)
    if len(listB) >= 2:
        listB = merge_sort(listB, iter + 1)
    print('About to merge!\n{0}\tand\t{1}'.format(listA, listB))
    return merge_arrays(listA, listB)


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
            merged_list.append(list1[idx1])
            idx1 += 1
        else:
            merged_list.append(list2[idx2])
            idx2 += 1
    else:
        # When one list is finished,
        # Append rest of other list to the final list
#        print(idx1, len(list1), idx2, len(list2))

        if idx1 == len(list1):
            for idx in list2[idx2:]:
                merged_list.append(idx)
        else:
            for idx in list1[idx1:]:
                merged_list.append(idx)

    return merged_list
       

def main():
    args = get_args()
    list_to_sort = parse_input(args.input)
    merged_list = merge_sort(list_to_sort, 0)
    with open(args.output, 'w') as file:
       file.write(' '.join([str(x) for x in merged_list]))


if __name__ == '__main__':
    main()

