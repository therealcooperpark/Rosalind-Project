#! /usr/bin/env python3

import Bio.SeqIO

def transversion_check(nuc, nuc2):
    if nuc == "A" or nuc == "G":
        if nuc2 == "C" or nuc2 == "T":
            return True

    if nuc == "C" or nuc == "T":
        if nuc2 == "A" or nuc2 == "G":
            return True

    return False

count = 0
for record in Bio.SeqIO.parse("sample.fa", "fasta"):
    if count == 0:
        seq1 = record
        count += 1
    else:
        seq2 = record

transitions = 0
transversions = 0

for index, nuc in enumerate(seq1):
    nuc2 = seq2[index]
    if nuc == nuc2:
        continue

    if transversion_check(nuc, nuc2):
        transversions += 1
    else:
        transitions += 1


print(transitions/transversions)
