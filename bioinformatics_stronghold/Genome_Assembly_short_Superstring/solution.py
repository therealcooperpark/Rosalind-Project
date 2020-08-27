#! /usr/bin/env python3
'''
Perform a shortest substring condensation
Under the assumption that each read can overlap with another with at least 1/2 its length
'''

import Bio.SeqIO

def parse_fasta(filepath):
    '''
    Parse fasta file, return sequences
    '''

    seqs = []
    for record in Bio.SeqIO.parse(filepath, "fasta"):
        seqs.append(str(record.seq))
    return seqs


def shortest_string(seqs):
    '''
    iterate over seqs to find shortest superstring
    '''

    superstring = seqs.pop()
    list_len = len(seqs)

    while len(seqs) != 0:
        # Iterate over all the seqs
        for sequence in list(seqs):
            # See if the prefix of one seq is the suffix of another
            # In either direction, largest overlap to shortest (min = len(seq)/2)
            for frame in range(len(sequence), len(sequence)//2, -1):
                if sequence.endswith(superstring[:frame]):
                    superstring = sequence + superstring[frame:]
                    seqs.remove(sequence)
                    break

                elif superstring.endswith(sequence[:frame]):
                    superstring = superstring + sequence[frame:]
                    seqs.remove(sequence)
                    break

        # If nothing changed, no superstring possible
        if len(seqs) == list_len:
            return None
        else:
            list_len = len(seqs)

    return superstring


def write_seq(substring):
    '''
    Write string to file
    '''

    with open("sequence.txt", "w") as output:
        output.write(substring)


def main():
    filepath = input("Enter fasta filepath:\n")
    seqs = parse_fasta(filepath)
    shortest_substring = shortest_string(seqs)
    if shortest_substring:
        write_seq(shortest_substring)
    else:
        print("Cannot use all seqs to generate shortest substring")


if __name__ == "__main__":
    main()
