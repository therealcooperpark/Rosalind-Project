#! /usr/bin/env python3

import Bio.SeqIO

def parse_fasta(filepath):
    '''
    Parse fasta file, return dictionary of read counts
    '''

    seqs = {}
    for record in Bio.SeqIO.parse(filepath, "fasta"):
        rev_seq = rev_comp(record.seq)
        if record.seq in seqs.keys():
            seqs[record.seq] += 1
        elif rev_seq in seqs.keys():
            seqs[rev_seq] += 1
        else:
            seqs.setdefault(str(record.seq), 1)

    return seqs


def rev_comp(sequence):
    '''
    Return reverse complement of a sequence
    '''

    rev_seq = ""
    for nuc in sequence[::-1]:
        if nuc == "A":
            rev_seq += "T"
        elif nuc == "T":
            rev_seq += "A"
        elif nuc == "C":
            rev_seq += "G"
        elif nuc == "G":
            rev_seq += "C"
    return rev_seq


def find_error_seqs(sequences):
    '''
    Find sequences with nucleotide errors
    '''
    corrections = {} # {Error:Corrected Read}

    potential_errors = [x for x in sequences.keys() if sequences[x] == 1]
    confirmed_reads = [x for x in sequences.keys() if sequences[x] > 1]
    for singleton in potential_errors:
        for good_read in confirmed_reads:
            rev_good_read = rev_comp(good_read)
            if hamming_distance(singleton, good_read) == 1:
                corrections[singleton] = good_read
            elif hamming_distance(singleton, rev_good_read) == 1:
                corrections[singleton] = rev_good_read
    return corrections


def hamming_distance(read1, read2):
    '''
    Calculate hamming distance between two reads
    '''
    return sum([1 for x in range(len(read1)) if read1[x] != read2[x]])


def write_output(corrected_reads):
    '''
    Write corrected read output to file
    '''
    with open("answer.txt", "w") as output:
        for read,value in corrected_reads.items():
            output.write("{0}->{1}\n".format(read,value))


def main():
    filepath = input("Enter fasta filepath:\n")
    sequences = parse_fasta(filepath)
    corrected_reads = find_error_seqs(sequences)
    write_output(corrected_reads)


if __name__ == "__main__":
    main()
