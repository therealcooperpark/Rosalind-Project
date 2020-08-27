#! /usr/bin/env python3
'''
Generate a DeBruijn Graph given DNA strings of (k+1)-mers
'''

def parse_file(filepath):
    '''
    Parse a file containing sequences
    return a set of sequences and their reverse compliment
    '''

    sequences = set()

    with open(filepath, "r") as file:
        for line in file:
            sequences.add(line.strip())
            sequences.add(rev_comp(line.strip()))
    return sequences


def rev_comp(sequence):
    '''
    Return reverse compliment of sequence
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


def make_graph(sequences):
    '''
    Make a De Bruijn graph with the given sequences
    They are (k+1)-mers
    '''

    directed_edges = {}
    for seq in sequences:
        kmer1 = seq[:-1]
        kmer2 = seq[1:]
        directed_edges.setdefault(kmer1, set())
        directed_edges[kmer1].add(kmer2)
    return directed_edges


def write_edges(directed_edges):
    '''
    Write directed edges out to file
    '''

    with open("answer.txt", "w") as output:
        for edge in directed_edges:
            for node in directed_edges[edge]:
                output.write("({0},{1})\n".format(edge, node))


def main():
    filepath = input("Enter path to file:\n")
    sequences = parse_file(filepath)
    debruijn = make_graph(sequences)
    write_edges(debruijn)

if __name__ == "__main__":
    main()
