#! /usr/bin/env python3

'''
Create a distance matrix from FASTA file sequences of the same length
'''
import Bio.SeqIO


def load_seqs(file):
    # Parse sequences from fasta file
    # Return dict of sequences and sequence order
    sequences = {}
    seq_order = []

    for record in Bio.SeqIO.parse(file, "fasta"):
        sequences[record.id] = record.seq
        seq_order.append(record.id)
    return sequences, seq_order


def calculate_distances(sequences):
    # Take dict of sequences, calculate all pairwise distances
    # Return dict of pairwise distances
    distances = {}

    for seq in sequences:
        for seq2 in sequences:
            key = "{0}:{1}".format(seq, seq2)
            dist = distance(sequences[seq], sequences[seq2])
            distances[key] = dist
    return distances


def distance(seq, seq2):
    # Calculate number of differences between 2 strings
    # Return differences/length of strings
    distance = 0
    for idx, nuc in enumerate(seq):
        if nuc != seq2[idx]:
            distance += 1
    return distance/len(seq)


def write_matrix(seq_order, distances):
    # Take all pairwise distances, write matrix grid of values
    with open("output_matrix.txt", "w") as output:
        for seq in seq_order:
            line = []
            for seq2 in seq_order:
                key = "{0}:{1}".format(seq, seq2)
                line.append(str(distances[key]))
            output.write("{0}\n".format(" ".join(line)))


def main():
    file = input("enter file location:\n")
    sequences, seq_order = load_seqs(file)
    distances = calculate_distances(sequences)
    write_matrix(seq_order, distances)


if __name__ == "__main__":
    main()
