#! /usr/bin/env python3
'''
Calculate minimum reversal distance
'''

def parse_file(filepath):
    '''
    parse file into pairs of lines for analysis
    '''
    with open(filepath, "r") as file:
        reversal_pairs = []
        line_count = 1
        for line in file:
            if line_count % 3 == 1:
                template = [int(x) for x in line.strip().split()]
            elif line_count % 3 == 2:
                query = [int(x) for x in line.strip().split()]
                reversal_pairs.append((template, query))
            line_count += 1

    return reversal_pairs


def calculate_reversal_dist(seq1, seq2):
    '''
    Calculate minimum reversal distance between pair
    '''

    inverse = inverse_permutation(seq2)
    seq1 = apply_permutation(inverse, seq1)
    reversal_count = 0

    print("-" * 24)

    for idx in range(len(seq1), 1, -1):
        for idx2 in range(len(seq1)):
            if seq1[idx2] == idx:
                break

        if idx - idx2 > 1:
            print(' '.join([str(0) if x == 10 else str(x) for x in seq1]), ":", idx)
            print(' '.join(([' ']*idx2) + (['-'] * (idx - idx2))))
            seq1[idx2:idx] = reversed(seq1[idx2:idx])
            reversal_count += 1

    return reversal_count


def inverse_permutation(original):
    '''
    Generate the inverse permutation
    (Swap values in list with their index position)
    '''

    inverse = [None for _ in range(len(original))]
    for idx, value in enumerate(original):
        inverse[value - 1] = idx + 1
    return inverse


def apply_permutation(original, mutator):
    '''
    Use mutator to apply permutation to original sequence
    '''

    new_sequence = []
    for num in mutator:
        new_sequence.append(original[num - 1])
    return new_sequence


def main():
    filepath = input("Enter path to dataset file:\n")
    reversal_pairs = parse_file(filepath)
    print(reversal_pairs)
    reversal_counts = []
    for pair in reversal_pairs:
        reversal_counts.append(calculate_reversal_dist(pair[0], pair[1]))
    print(" ".join([str(x) for x in reversal_counts]))


if __name__ == "__main__":
    main()
