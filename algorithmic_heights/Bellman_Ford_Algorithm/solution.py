#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    return parser.parse_args()


def parse_graph(graph_file):
    ''' Parse graph into dict of paths and weights '''

    graph = {}

    with open(graph_file, 'r') as file:
        # Take graph stats (# nodes, # edges)
        # Set nodes in graph w/ no edges
        graph_stats = file.readline().strip().split()
        for node in range(int(graph_stats[0])):
            graph.setdefault(int(node)+1, [])
        # Add edge tuples (edge ID, weight) to nodes
        for line in file:
            line = line.strip().split()
            graph[int(line[0])].append((int(line[1]), int(line[2])))
    return graph


def bellman(graph):
    '''
    Use bellman-ford algorithm to find shortest path through
    weighted directed graph with negative edges
    '''

    # Set starter numbers
    graph_dists = [0]
    graph_dists.extend( [1001 for _ in range(len(graph) - 1)] )
    check_nodes = set()
    check_nodes.add(1)

    # Do Bellman-Ford algorithm
    # Iterate over num of nodes - 1
    for iter in range(len(graph) - 1):
        new_check_nodes = set() # List of nodes to check in next iter

        # Check every neccessary node for shorter dist
        for node in check_nodes:
            std_weight = graph_dists[node - 1]
            for edge, weight in graph[node]:

                # If found, update dists, add node to future checks
                if weight + std_weight < graph_dists[edge - 1]:
                    graph_dists[edge - 1] = weight + std_weight
                    new_check_nodes.add(edge)

        # Update set of nodes to check
        check_nodes = new_check_nodes

    return [str(x) if x < 1001 else 'x' for x in graph_dists]


def main():
    args = get_args()
    graph = parse_graph(args.input_file)
    shortest_dists = bellman(graph)
    print(' '.join(shortest_dists))

if __name__ == '__main__':
    main()
