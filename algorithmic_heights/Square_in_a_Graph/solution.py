#! /usr/bin/env python3

from argparse import ArgumentParser
from itertools import combinations


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    return parser.parse_args()


def adj_matricies(graphs):
    ''' Parse list of text string graphs into adj matricies '''

    adj_matricies = []
    for graph in graphs:
        # Make matrix
        graph = graph.split('\n')
        adj_matricies.append({})
        # Fill matrix with nodes and empty edges
        graph_stats = graph[0].split()
        for node in range(int(graph_stats[0])):
            adj_matricies[-1].setdefault(node, [])
        # Fill matrix with known edges
        for pair in graph[1:]:
            x, y = pair.split()
            x, y = int(x), int(y)
            adj_matricies[-1][x-1].append(y-1)
            adj_matricies[-1][y-1].append(x-1)
    return adj_matricies


def find_square(mtx):
    ''' Find cycle of size 4, if not, return -1 '''

    connected_pairs = set()

    for node in mtx:
        # If pair combination exists in set, then 4 points
        # can be linked together.
        for node1, node2 in combinations(mtx[node], 2):
            node_pair = (node1, node2)
            if node_pair in connected_pairs:
                return '1'
            else:
                connected_pairs.add(node_pair)
    return '-1'


def main():
    # Parse graphs from file into adj. matricies
    args = get_args()
    file = open(args.input_file, 'r')
    adj_mtx = adj_matricies(file.read().strip().split('\n\n')[1:])
    answer = []
    for mtx in adj_mtx:
        answer.append(find_square(mtx))

    print(' '.join(answer))
if __name__ == '__main__':
    main()
