#! /usr/bin/env python3
'''
Count the number of missing edges from a complete tree
purely mathematical... No actual tree building
'''

def parse_tree_file(filepath):
    edge_count = 0
    with open(filepath, "r") as file:
        total_nodes = int(file.readline().strip())
        for line in file:
            edge_count += 1
    return total_nodes - edge_count - 1


def main():
    filepath = input("Enter path to rosalind data file:\n")
    print(parse_tree_file(filepath))


if __name__ == "__main__":
    main()
