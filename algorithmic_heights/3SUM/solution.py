#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file', help = 'rosalind input file')
    parser.add_argument('output_file', help = 'output file for rosalind')
    return parser.parse_args()


def parse_input(input_file):
    '''
    Parse input file into list of tuples
    Each tuple has 2 lists, one negatives,
    one positives
    '''

    arrays = []

    with open(input_file, 'r') as file:
        next(file)
        for line in file:
            negs = []
            pos = []
            idxs = {}
            order = [int(num) for num in line.strip().split()]
            for idx, num in enumerate(order):
                idxs.setdefault(num, [])
                idxs[num].append(idx)
                if num < 0:
                    negs.append(num)
                else:
                    pos.append(num)
            arrays.append( (negs, pos, idxs) )
    return arrays


def find_threesum(array):
    '''
    Find 3 numbers that sum to zero
    '''

    pos, neg, order = array[0], array[1], array[2]

    # Get two numbers, try to find the third in the dict
    for pos_num in pos:
        for neg_num in neg:
            leftover = pos_num + neg_num
            try:
                idx_3 = order[-leftover][0]
            except KeyError:
                continue

            # Get index of other two numbers, sort and return them
            idx_1 = order[pos_num][1] if pos_num == leftover else order[pos_num][0]
            idx_2 = order[neg_num][1] if neg_num == leftover else order[neg_num][0]
            idx_order = [idx_1, idx_2, idx_3]
            idx_order.sort()
            print('FOUND')
            return [str(x+1) for x in idx_order]

    # If all failed, return -1
    print('FAILED')
    return ['-1']


def write_output(answers, output_file):
    '''
    Write output file for rosalind
    '''

    with open(output_file, 'w') as file:
        for answer in answers:
            file.write(' '.join(answer) + '\n')


def main():
    args = get_args()
    arrays = parse_input(args.input_file)
    answers = []
    for x in arrays:
        answers.append(find_threesum(x))
        print('------------------------')

    write_output(answers, args.output_file)


if __name__ == '__main__':
    main()
