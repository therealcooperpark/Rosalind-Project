#! /usr/bin/env python3

import Bio.SeqIO

count = 0
for record in Bio.SeqIO.parse("sample.fa", "fasta"):
    if count == 0:
        string = record
        count += 1
    else:
        motif = record

complete_motif = False
motif_index = 0
indices = []
for index, nuc in enumerate(string):
    if nuc == motif.seq[motif_index]:

        if motif_index == len(motif.seq) - 1:
            complete_motif = True

        motif_index += 1
        indices.append(index + 1)

    if complete_motif:
        print(indices)
        break
