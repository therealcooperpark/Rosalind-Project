#! /usr/bin/env python3

class Tree:
    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def new_node(self, node):
        self.nodes.append(node)

    def new_edge(self, edge):
        self.edges.append(edge)

    def merge_trees(self, tree):
        self.nodes = self.nodes.union(tree.nodes)
        self.edges = self.edges.union(tree.edges)
        tree.nodes = set()
        tree.edges = set()


trees = []
all_nodes = set()

with open("dataset.txt", "r") as file:
    total_nodes = int(file.readline().strip())

    for line in file:
        nodes = line.strip().split()
        good_tree = None
        for node in nodes:
            all_nodes.add(node)
            for idx, tree in enumerate(trees):
                if node in tree.nodes:
                    good_tree = idx
                    trees[idx].nodes.add(nodes[0])
                    trees[idx].nodes.add(nodes[1])
                    trees[idx].edges.add( (nodes[0], nodes[1]) )

            if not good_tree:
                trees.append(Tree())
                trees[-1].nodes.add(nodes[0])
                trees[-1].nodes.add(nodes[1])
                trees[-1].edges.add( (nodes[0], nodes[1]) )

for tree in trees:
    other_trees = list(trees)
    other_trees.remove(tree)
    for tree2 in other_trees:
        same = tree.edges.intersection(tree2.edges)
        if len(same) > 0:
            tree.merge_trees(tree2)

for tree in list(trees):
    if len(tree.nodes) == 0:
        trees.remove(tree)

print(total_nodes - len(all_nodes) + len(trees) - 1)
