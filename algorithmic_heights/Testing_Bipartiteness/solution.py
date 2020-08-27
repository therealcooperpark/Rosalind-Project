#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    return parser.parse_args()


def parse_input(input_file):
    ''' Parse input into list of graphs to parse '''

    with open(input_file, 'r') as file:
        next(file)
        next(file)

        # Get edge lists in raw format
        to_parse = file.read().split('\n\n')
    return to_parse


def bipartite_check(raw_edge_list):
    ''' Check graph for bipartiteness '''

    graph = parse_graph(raw_edge_list)
    traversal = {x:False for x in graph} # Checks traversal for node
    node_group = {}


    for node in graph:
        if not traversal[node]: # Don't do a node twice
            traversal, bipartiteness = depth_first_search(node, graph, traversal, 'A', 'B')
        if bipartiteness == '-1': # Auto return -1 if found
            return bipartiteness
    return bipartiteness


def parse_graph(raw_edge_list):
    ''' Parse graph from edge list '''

    graph = {}

    raw_edge_list = raw_edge_list.rstrip().split('\n')

    # Build basic dict for graph
    graph_stats = raw_edge_list[0]
    for x in range(1, int(graph_stats.split()[0])+1):
        graph.setdefault(x, set())

    for pair in raw_edge_list[1:]: # Skips the format line
        pair = pair.split()
        # Add one direction of the pair
        graph[int(pair[0])].add(int(pair[1]))
        # Add opposite direction (undirected graph)
        graph[int(pair[1])].add(int(pair[0]))
    return graph


def depth_first_search(parent, graph, traversal, group, opp_group):
    ''' Recursively bin nodes and look for conflicts '''

    # Check if traversal has occurred for parent node...

    # If not yet, set parent to group
    if not traversal[parent]:
        traversal[parent] = group
        bi_check = '1'
        for edge in graph[parent]:
            traversal, bi_check = depth_first_search(edge, graph, traversal, opp_group, group)
            if bi_check == '-1':
                return traversal, bi_check # Auto fail when -1 found
        return traversal, bi_check # Send back a good sign if no failures

    # If traversed and doesn't match, fail the bipartite check
    elif traversal[parent] != group:
        return traversal, '-1'

    # If traversed and matches, send back a good signal
    else:
        return traversal, '1'


def main():
    args = get_args()
    raw_edge_lists = parse_input(args.input_file)
    for edge_list in raw_edge_lists: # -1 skips last empty line
        print(bipartite_check(edge_list), end = ' ')
    print()

if __name__ == '__main__':
    main()
