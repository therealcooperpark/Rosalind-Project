#! /usr/bin/env python3
'''
Replicate the Knuth-Morris-Pratt algorithm pre-processing step
to identify the longest kmer at each index of a given string
'''

def parse_file(filepath):
    '''
    Get the sequence from file
    '''

    sequence = ""
    with open(filepath, "r") as file:
        for line in file:
            if line[0] == ">":
                continue
            else:
                sequence += line.strip()
    return sequence


def build_failure_array(sequence):
    '''
    Use the KMP pre-processing script
    '''

    failure_array = [0]
    motif_len = 0
    idx = 1
    while idx < len(sequence):
        if sequence[idx] == sequence[motif_len]:
            motif_len += 1
            failure_array.append(motif_len)
            idx += 1
        else:
            if motif_len != 0:
                motif_len = failure_array[motif_len - 1]
            else:
                failure_array.append(motif_len)
                idx += 1
    return failure_array


def write_output(array):
    '''
    Write array onto single line in file
    '''

    with open("answer.txt", "w") as output:
        output.write(" ".join([str(x) for x in array]))


def main():
    filepath = input("Enter path to FASTA file:\n")
    sequence = parse_file(filepath)
    array = build_failure_array(sequence)
    write_output(array)


if __name__ == "__main__":
    main()
