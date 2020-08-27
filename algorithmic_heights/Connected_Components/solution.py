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

    graph = {}

    with open(input_file, 'r') as file:
        line = file.readline().strip().split()
        for i in range(1, int(line[0])+1): # Iterate over possible nodes and add to graph
            graph.setdefault(i, [])

        for line in file: # Iterate over edge list and build graph
            line = line.strip().split()
            graph[int(line[0])].append(int(line[1]))
            graph[int(line[1])].append(int(line[0]))
    return graph


def depth_first_search(graph):
    '''
    Count all connected components to a graph
    '''

    traversal = {node:False for node in range(1, max(graph)+1)}
    component_count = 1
    components = set()

    # Explore all nodes
    for idx in range(1, max(graph)+1):
        # Build a stack starting with first node
        stack = [idx]

        # Pull a node from stack
        # Check traversal
        # Add component number if not traversed
        while len(stack) > 0:
            node = stack.pop()
            if not traversal[node]:
                traversal[node] = component_count
                components.add(component_count)
                for edge in graph[node]:
                    stack.append(edge)

        # Update component count before next node
        component_count += 1

    # Return component dict and number of unique components
    return traversal, len(components)


def main():
    args = get_args()
    graph = parse_input(args.input_file)
    traversal, components = depth_first_search(graph)
    print(components)


if __name__ == '__main__':
    main()
