#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    return parser.parse_args()


def parse_input(input_file):
    ''' Parse input file into array '''

    with open(input_file, 'r') as file:
        next(file)
        heap_list = list(map(int, file.readline().strip().split()))
    return heap_list


def heapify(heap_list):
    ''' turn array into max heap '''
    # Taken from Mr. Drake @ rosalind.info/problems/hea/solutions/
    # Because it's far more clean than my implementation

    for idx in range(1, len(heap_list)):
        cur_idx = idx
        while cur_idx > 0 and heap_list[cur_idx] > heap_list[(cur_idx-1)//2]:
            heap_list[cur_idx], heap_list[(cur_idx-1)//2] = heap_list[(cur_idx-1)//2], heap_list[cur_idx]
            cur_idx = (cur_idx-1)//2
    return heap_list


def heap_sort(max_heap):
    ''' Perform heap sort '''

    sorted_values = []
    
    while len(max_heap) > 0:
        # Swap first and last value, pop highest value from heap
        max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0]
        sorted_values.append(max_heap.pop())

        idx = 0
        while idx < len(max_heap):
            # Find largeest value
            c1, c2 = 2*idx+1, 2*idx+2
            if c1 < len(max_heap):
                if c2 < len(max_heap):
                    large = max([max_heap[idx], max_heap[c1], max_heap[c2]])
                else:
                    large = max([max_heap[idx], max_heap[c1]])
            elif c2 < len(max_heap):
                large = max([max_heap[idx], max_heap[c2]])
            else:
                large = max_heap[idx]

            # Move parent in the right direction. End while-loop if parent is good
            if c1 < len(max_heap) and large == max_heap[c1]:
                max_heap[c1], max_heap[idx] = max_heap[idx], max_heap[c1]
                idx = c1
            elif c2 < len(max_heap) and large == max_heap[c2]:
                max_heap[c2], max_heap[idx] = max_heap[idx], max_heap[c2]
                idx = c2
            else:
                break

    print(*sorted_values[::-1])


def main():
    args = get_args()
    heap_list = parse_input(args.input_file)
    max_heap = heapify(heap_list)
    heap_sort(max_heap)

if __name__ == '__main__':
    main()
