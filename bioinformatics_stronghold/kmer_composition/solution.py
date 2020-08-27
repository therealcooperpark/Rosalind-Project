#! /usr/bin/env python3

import Bio.SeqIO
import itertools

# Read in the data
record = Bio.SeqIO.read("dataset.txt", "fasta")

# Make dictionary of all kmers
kmers = {}
for kmer in itertools.product("ACTG", repeat=4):
    kmer = "".join(list(kmer))
    kmers.setdefault(kmer, 0)

# Count Kmers
for idx in range(len(record.seq) - 3):
    kmer = str(record.seq[idx:idx+4])
    kmers[kmer] += 1

# Alphabetical kmers
unique = sorted(list(kmers.keys()))

# Write out
with open("answer.txt", "w") as output:
    for kmer in unique:
        output.write("{0} ".format(kmers[kmer]))
