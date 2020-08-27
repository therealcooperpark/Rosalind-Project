#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    return parser.parse_args()


def parse_graphs(graph_file):
    ''' Parse graph into dict of paths and weights '''

    graphs = []

    with open(graph_file, 'r') as file:
        graph_num = int(file.readline().strip()) # Number of graphs
        for i in range(graph_num):
            # Take graph stats (# nodes, # edges)
            # Set nodes in graph w/ no edges
            graph = {}
            graph_stats = file.readline().strip().split()
            node_num = int(graph_stats[0])
            for node in range(int(graph_stats[0])):
                graph.setdefault(int(node)+1, [])

            # Add edge tuples (edge ID, weight) to nodes
            for l in range(int(graph_stats[1])):
                line = file.readline().strip().split()
                graph[int(line[0])].append((int(line[1]), int(line[2])))

            graphs.append(graph)
    return graphs


def is_negative_cycle(graph):
    '''
    Use bellman-ford algorithm to find negative weight cycle
    in weighted negative edge directed graph
    '''

    # Set starter numbers
    graph_dists = [0]
    graph_dists.extend( [1001 for _ in range(len(graph) - 1)] )
    check_nodes = set()
    for node in graph:
        check_nodes.add(node) # Add all nodes, no assumed start path

    # Do Bellman-Ford algorithm
    # Iterate over num of nodes
    for iter in range(len(graph)):
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

        # Grab final iteration values, before negative cycle test
        if iter + 1 == len(graph) - 1:
            final_dists = list(graph_dists)

    # compare graph_dists to final_dists
    # If the same, no cycle, else negative cycle
    for idx, val in enumerate(graph_dists):
        if val < final_dists[idx]:
            return '1'

    else:
        return '-1'


def main():
    args = get_args()
    graphs = parse_graphs(args.input_file)

    answers = []
    for graph in graphs:
        answers.append(is_negative_cycle(graph))

    print(' '.join(answers))

if __name__ == '__main__':
    main()
