#! /usr/bin/env python3
'''
Count the number of internal nodes in an unrooted tree
Given the number of leaf nodes
'''


def internal_nodes(leafs):
    # Internal nodes = leafs - 2
    return leafs - 2


def main():
    leafs = int(input("Enter the number of tree leafs:\n"))

    print(internal_nodes(leafs))


if __name__ == "__main__":
    main()
