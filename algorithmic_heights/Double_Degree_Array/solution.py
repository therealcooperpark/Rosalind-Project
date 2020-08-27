#! /usr/bin/env python3

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input', help = 'input file')
    parser.add_argument('output', help = 'output file name')
    return parser.parse_args()


def parse_input(input_file):
    '''
    Parse edge list into dictionary
    Key = node
    Value = list of nodes attached to Key
    '''

    graph = {}

    with open(input_file, 'r') as file:
        parameters = file.readline().strip().split()
        maximum_value = int(parameters[0])

        for line in file: 
            line = [int(x) for x in line.strip().split()]
            graph.setdefault(line[0], set())
            graph[line[0]].add(line[1])
            graph.setdefault(line[1], set())
            graph[line[1]].add(line[0])

    return maximum_value, graph


def write_output(max, graph, out):
    '''
    Write output in node order small to large
    '''

    with open(out, 'w') as output:
        for node in range(1, max+1):
            degree_sum = 0

            try:
                for neighbor in graph[node]:
                    degree_sum += len(graph[neighbor])
            except KeyError:
                pass

            output.write(str(degree_sum) + ' ')



def main():
    args = get_args()
    maximum_value, graph = parse_input(args.input)

    print(graph)
    write_output(maximum_value, graph, args.output)


if __name__ == "__main__":
    main()
