#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    return parser.parse_args()


def parse_input(input_file):
    ''' Parse edge list format into directed graph '''

    graph = {}
    with open(input_file, 'r') as file:
        node_count = file.readline().strip().split()[0]

        # Set default empty list for each node
        for x in range(1, int(node_count)+1):
            graph.setdefault(x, [])

        # Add edges to graph
        for line in file:
            line = line.strip().split()
            graph[int(line[0])].append(int(line[1]))
    return graph


def find_topology(graph):
    ''' Find topological order for acyclic directed graph '''

    post_values = [] # Track post values for each node
    
    # Iterate over every node and do a depth-first analysis
    for idx in range(1, max(graph)+1):
        post = 0
        stack = [idx]

        # Depth-first search
        while len(stack) > 0:
            node = stack.pop()
            
            # Add edges to stack, tally posts
            for edge in graph[node]:
                stack.append(edge)
                post += 1

        # Update post value for idx
        post_values.append( (idx, post) )

    post_values.sort(key = lambda x: x[1], reverse = True)
    return post_values


def main():
    args = get_args()
    graph = parse_input(args.input_file)
    topological_order = find_topology(graph)
    with open(args.output_file, 'w') as file:
        out = [str(x[0]) for x in topological_order]
        file.write(' '.join(out))


if __name__ == '__main__':
    main()
