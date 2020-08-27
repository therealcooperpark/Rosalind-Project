#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file', help = 'input file from rosalind')
    parser.add_argument('output_file', help = 'output file for rosalind')
    return parser.parse_args()


def parse_input(input_file):
    '''
    Parse input file into a directed graph
    '''

    graph = {} # Key is node, value is list of edges

    with open(input_file, 'r') as file:

        # Use node count to establish nodes on graph
        line = file.readline().strip().split()
        num_nodes = int(line[0])
        for i in range(num_nodes):
            graph.setdefault(i+1, [])

        # Parse edge list to build graph
        for line in file:
            line = line.strip().split()
            node1, node2 = int(line[0]), int(line[1])
            graph[node1].append(node2)
    return num_nodes, graph


def breadth_first_search(graph, target):
    '''
    Using the target node, find shortest distance to all possible nodes
    Impossible routes are not represented in the returned dict
    Assume no loops are present
    '''

    shortest_paths = {target:0} # Dict of shortest distance to target node
    node_queue = [target] # Queue to iterate over nodes

    nodes = set()

    while len(node_queue) > 0:
        node = node_queue.pop()
        print(node)
        nodes.add(node)

        for link in graph[node]:
            if link not in nodes:
                node_queue.insert(0, link)
                shortest_paths.setdefault(link, shortest_paths[node] + 1)
    return shortest_paths


def main():
    args = get_args()
    num_nodes, graph = parse_input(args.input_file)
    shortest_paths = breadth_first_search(graph, 1)
    with open(args.output_file, 'w') as file:
        for node in range(1, num_nodes+1):
            try:
                dist = str(shortest_paths[node])
            except KeyError:
                dist = '-1'
            file.write('{0} '.format(dist))
        file.write('\n')


if __name__ == '__main__':
    main()
