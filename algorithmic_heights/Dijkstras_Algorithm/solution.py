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


def dijkstras(graph):
    ''' 
    Use dijkstras algorithm to find shortest path through
    weighted directed graph
    '''

    # Establish starting dists
    graph_dists = ['0']
    graph_dists.extend( ['-1' for _ in range(len(graph) - 1)] )
    short_graph = set()
    short_graph.add(1)

    # Do dijkstras
    while len(short_graph) < len(graph):
        print(' ----- ')
        print(' '.join(graph_dists))
        # Check each edge for shortest path
        shortest_path = 1001 # Maximum edge weight is 1000
        short_vertex, set_node  = None, None
        for node in short_graph:
            print('{0}\t{1}'.format(node, graph[node]))
            for edge in graph[node]:
                if edge[1] < shortest_path and edge[0] not in short_graph:
                    shortest_path, short_vertex, set_node = edge[1], edge[0], node

        # If no shortest path found, close out
        if not short_vertex:
            break
        else:
            short_graph.add(short_vertex)
            graph_dists[short_vertex - 1] = str(shortest_path + int(graph_dists[set_node - 1]))

    return graph_dists


def main():
    args = get_args()
    graph = parse_graph(args.input_file)
    shortest_dists = dijkstras(graph)
    print(' '.join(shortest_dists))

if __name__ == '__main__':
    main()
