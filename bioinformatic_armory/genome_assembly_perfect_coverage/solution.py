#! /usr/bin/env python3
'''
Assemble a genome under the assumption of perfect coverage
'''


import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('kmer_list', help = 'list of kmers to assemble')
    return parser.parse_args()


def parse_kmers(kmer_file):
    with open(kmer_file, 'r') as file:
        return [x.strip() for x in file.readlines()]


def build_debruijn_graph(sequences):
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


def build_genome(debruijn_graph):
    '''
    Build a genome with perfect coverage
    '''

    first_kmer = list(debruijn_graph.keys())[0] # Pull a random kmer to start
    genome = first_kmer[0]
    next_kmer = list(debruijn_graph[first_kmer])[0] # Get next kmer to start the while-loop

    while next_kmer != first_kmer: # Go through the cycle
        print('Genome: {0}\nfirst_kmer: {1}\nnext_kmer: {2}'.format(genome, first_kmer, next_kmer))
        genome += next_kmer[-1]
        next_kmer = list(debruijn_graph[next_kmer])[0]
    return genome
    

def main():
    args = get_args()
    kmer_list = parse_kmers(args.kmer_list)
    debruijn_graph = build_debruijn_graph(kmer_list) # Skip revcomp seqs for now...
    genome = build_genome(debruijn_graph)
    print(genome)

if __name__ == '__main__':
    main()

