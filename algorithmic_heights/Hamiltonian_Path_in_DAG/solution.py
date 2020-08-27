#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    return parser.parse_args()


def parse_input(input_file):
    ''' Parse input into list of graphs to parse further '''

    # List of tuples: (graph, potential_sources)
    graphs = []

    # Open file and skip first two lines
    with open(input_file, 'r') as file:
        next(file)
        next(file)

        # Parse graphs and append completed graph
        # to list
        first_line = True # Skips first line of each graph
        for line in file:
            if line == '\n':
                graphs.append( (graph, list(sources.difference(not_sources))) )
                first_line = True
                continue

            elif first_line: # Parse first line of each graph (graph stats)
                first_line = False
                line = line.strip().split()
                graph = {x:[] for x in range(1, int(line[0])+1)}
                sources = set([x for x in range(1, int(line[0])+1)]) # Set of nodes with no parent
                not_sources = set()
                continue

            # Parse edge list format
            else:
                line = line.strip().split()
                graph[int(line[0])].append(int(line[1]))
                not_sources.add(int(line[1])) # Must have parent, remove from sources
    graphs.append( (graph, list(sources.difference(not_sources))) )
    return graphs


def find_hamiltonian(graph, potential_sources):
    ''' 
    Find a potential hamiltonian path in
    simple directed acyclic graph.
    Return 1 and path if found, else -1
    '''

    max_path_log = {x:False for x in graph} # Tracks the longest path + path for each node to avoid doing it twice

    # Iterate over every node and do a depth-first analysis
    if len(potential_sources) > 1:
        return '-1'

    max_path, max_path_log = depth_search(graph, potential_sources[0], max_path_log)
    if max_path[1] == (len(graph) - 1):
        max_path[0].insert(0, '1')
        return ' '.join(max_path[0])

    return '-1'


def depth_search(graph, node, max_path_log):
    ''' Find longest distance traversable from node '''

    if graph[node] == []: # Base case. End of graph, return 0
        max_path_log[node] = [[str(node)], 0]
        return [[str(node)], 0], max_path_log

    potential_paths = [] # List of paths and distances in tuples
    for edge in graph[node]:
        if not max_path_log[edge]: # If never traversed
            path, max_path_log = depth_search(graph, edge, max_path_log)
            potential_paths.append(path)
        else: # Pull previously made longest path
            potential_paths.append( max_path_log[edge] )


    # Get longest path, add 1 to it (for this node) and send the highest back
    potential_paths.sort(key = lambda x: x[1], reverse = True)
    # Log path in dict
    max_path = potential_paths[0]
    max_path_log[node] = max_path
    # Update it with current node and send it back
    max_path[0].insert(0, str(node))
    max_path[1] += 1
    return max_path, max_path_log


def main():
    args = get_args()
    graphs = parse_input(args.input_file)
    hamiltonian_paths = []
    for graph in graphs:
        hamiltonian_paths.append( find_hamiltonian(graph[0], graph[1]) )
    with open(args.output_file, 'w') as file:
        for path in hamiltonian_paths:
            file.write(path + '\n')


if __name__ == '__main__':
    main()
