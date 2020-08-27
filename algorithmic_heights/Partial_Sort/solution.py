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
        k = int(file.readline().strip())
    return heap_list, k


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


def partial_sort(max_heap, others):
    ''' Perform heap sort '''

    while len(others) > 0:
#        print(max_heap)
        # Swap first and last value, pop highest value from heap
        val = others.pop()
        if val > max_heap[0]:
            continue

        max_heap[0] = val

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

    max_heap.sort()
    print(*max_heap)


def main():
    args = get_args()
    heap_list, k = parse_input(args.input_file)
    max_heap = heapify(heap_list[:k])
    partial_sort(max_heap, heap_list[k:])

if __name__ == '__main__':
    main()
