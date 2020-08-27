#! /usr/bin/env python3
'''
Do Merge Sort
'''

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input', help = 'input file from Rosalind')
    return parser.parse_args()


def parse_input(input_file):
    '''
    Parse two sorted lists from Rosalind file
    '''

    with open(input_file, 'r') as file:
        next(file)
        list_to_sort = [int(x) for x in file.readline().strip().split()]
    return list_to_sort


def merge_sort(list_to_sort):
    '''
    Recursively Merge arrays
    '''

    if len(list_to_sort) <= 1:
        return list_to_sort, 0

    midpoint = len(list_to_sort) // 2
    listA = list_to_sort[:midpoint]
    listB = list_to_sort[midpoint:]

    listA, A_inversions = merge_sort(listA)
    listB, B_inversions = merge_sort(listB)
    sorted_array, C_inversions = merge_arrays(listA, listB)

    return sorted_array, C_inversions+B_inversions+A_inversions


def merge_arrays(list1, list2):
    '''
    Merge two sorted lists together
    '''

    merged_list = []
    idx1, idx2 = 0, 0
    inversions = 0

    # merge the arrays
    while idx1 < len(list1) and idx2 < len(list2):
        # For most of lists, append lowest values at
        # Each index, increase lowest value idx by 1
        if list1[idx1] <= list2[idx2]:
            merged_list.append(list1[idx1])
            idx1 += 1
        else:
            merged_list.append(list2[idx2])
            inversions += len(list1) - idx1
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

    return merged_list, inversions
       

def main():
    args = get_args()
    list_to_sort = parse_input(args.input)
    merged_list, inversions = merge_sort(list_to_sort)
    print(inversions)


if __name__ == '__main__':
    main()

