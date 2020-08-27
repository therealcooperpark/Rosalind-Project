#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    return parser.parse_args()


def parse_input(input_file):
    '''
    Parse input file into graph
    '''

    graphs = []

    with open(input_file, 'r') as file:
        # Split file by double linefeed to separate graphs
        for graph in file.read().strip().split('\n\n')[1:]:

            # For each graph, build a graph dict and append to list
            lines = graph.split('\n')
            graph_stats = lines[0].split()
            tmp_graph = {}

            # Build nodes as keys with empty edge lists
            for x in range(1, int(graph_stats[0])+1):
                tmp_graph.setdefault(x, [])

            # For each edge in the file, add the edge to the dict
            for line in lines[1:]:
                line = line.strip().split()
                tmp_graph[int(line[0])].append(int(line[1]))
            graphs.append(tmp_graph)

    return graphs


def depth_first_search(graph):
    '''
    Find a cycle
    '''

    # Explore all nodes
    for idx in range(1, max(graph)+1):

        # Track if a node is picked up during each iteration of depth search
        traversal = {node:False for node in range(1, max(graph)+1)}

        # Build a stack starting with first node
        stack = [idx]

        # Pull a node from stack
        while len(stack) > 0:
            node = stack.pop()

            # Check traversal
            if not traversal[node]:
                traversal[node] = True

                # Add component number if not traversed, else confirm cyclicity
                for edge in graph[node]:
                    if edge == idx:
                        return -1
                    if not traversal[edge]:
                        stack.append(edge)

    # Return acyclic symbol
    return 1


def main():
    args = get_args()
    graphs = parse_input(args.input_file)
    for graph in graphs:
        traversal = depth_first_search(graph)
        print(traversal, end = ' ')
    print()

if __name__ == '__main__':
    main()
