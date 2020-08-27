#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    return parser.parse_args()


def parse_input(input_file):
    ''' Parse input file '''

    with open(input_file, 'r') as file:
        heap_len = int(file.readline().strip())
        child_dict = {} # Converts parent idx to children idx tuple
        parent_dict = {} # Converts child idx to parent idx
        for idx in range(heap_len):
            c1, c2 = 2*idx + 2, 2*idx + 1 # Define child indicies (2*idx + 1 AND 2*idx + 2)
            child_dict[idx] = (c1, c2)
            parent_dict[c1] = idx
            parent_dict[c2] = idx

        heap_list = [int(x) for x in file.readline().strip().split()]
    return heap_list, child_dict, parent_dict


def build_heap(heap_list, child_dict, parent_dict):
    ''' Sort heap for max heap property '''

    for num in range(1, len(heap_list)):
        idx = len(heap_list) - num # Work backwards through the list
        pidx = parent_dict[idx] # Pull parent's idx
        child, parent = heap_list[idx], heap_list[pidx]

        # If child larger than parent, swap and back check
        if child > parent:
            heap_list[idx], heap_list[pidx] = parent, child
            heap_list = back_check_heap(heap_list, idx, child_dict, parent_dict)
    return heap_list


def back_check_heap(heap_list, p_idx, child_dict, parent_dict):
    ''' Verify parent swap works with rest of heap '''

    # Get children and parent nodes
    c1_idx, c2_idx = child_dict[p_idx]
    c1 = heap_list[c1_idx] if c1_idx < len(heap_list) else None
    c2 = heap_list[c2_idx] if c2_idx < len(heap_list) else None
    parent = heap_list[p_idx]


    # Get largest value not including nones
    # If both none, return heap as-is
    if c1:
        if c2:
            largest = max([c1, c2, parent])
        else:
            largest = max([c1, parent])
    elif c2:
        largest = max([c2, parent])
    else:
        return heap_list

    # Swap largest value for parent, if parent is largest, stop
    if largest == c1:
        heap_list[c1_idx], heap_list[p_idx] = parent, c1
        return back_check_heap(heap_list, c1_idx, child_dict, parent_dict)
    elif largest == c2:
        heap_list[c2_idx], heap_list[p_idx] = parent, c2
        return back_check_heap(heap_list, c2_idx, child_dict, parent_dict)
    else: # largest == parent
        return heap_list


def self_check(heap, child_dict, parent_dict):
    ''' Check the heap to make sure it fits max heap properties '''

    problems = 0

    for idx, val in enumerate(heap):
        c1, c2 = child_dict[idx]
        try:
            if val >= heap[c1] and val >= heap[c2]:
               continue
            else:
                problems += 1
                print(val, heap[c1], heap[c2])
        except IndexError:
            print('Number of problems:', problems)
            break

def main():
    args = get_args()
    heap_list, child_dict, parent_dict = parse_input(args.input_file)
    heap = build_heap(heap_list, child_dict, parent_dict)
    self_check(heap, child_dict, parent_dict)

    with open(args.output_file, 'w') as file:
        out = ' '.join([str(x) for x in heap])
        file.write(out)


if __name__ == '__main__':
    main()
