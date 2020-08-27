#! /usr/bin/env python3

import Bio.SeqIO

def parse_file(filepath):
    '''
    Parse file as FASTA
    '''

    sequences = []
    for record in Bio.SeqIO.parse(filepath, "fasta"):
        sequences.append(str(record.seq))
    return sequences


def find_shared_motif(seq1, seq2):
    '''
    Find longest shared motif between two seqs
    '''

    short_seq = seq1 if len(seq1) < len(seq2) else seq2


def main():
    fasta = input("Enter filepath to fasta file:\n")
    sequences = parse_file(fasta)
    common_motif = find_shared_motif(sequences[0], sequences[1])


if __name__ == "__main__":
    main()
