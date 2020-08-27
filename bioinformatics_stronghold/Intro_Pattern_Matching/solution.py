#! /usr/bin/env python3
'''
Build a Trie from the given strings
Report the parent/child indicies and the value for each node
'''

class Node():
    def __init__(self, parent = None, value = None, index = None):
        self.parent = parent
        self.children = []
        self.value = value
        self.index = index

    def add_child(self, child):
        self.children.append(child)

    def children_values(self):
        children_tuples = []
        if len(self.children) == 0:
            return [[self.parent.index, self.index, self.value]]
        if self.value != None:
            children_tuples.append([self.parent.index, self.index, self.value])
        for child in self.children:
            children_tuples.extend(child.children_values())

        return children_tuples


class Tree():
    def __init__(self):
        self.root = Node(index = "1")


def make_trie(filepath):
    current_idx = 2
    Trie = Tree()
    with open(filepath, "r") as file:
        for line in file:
            string = line.strip()
            node = Trie.root
            for char in string:
                present = [x for x in node.children if char == x.value]
                if len(present) == 0:
                    node = Node(node, char, str(current_idx))
                    node.parent.add_child(node)
                    current_idx += 1
                else:
                    node = present[0]
    return Trie


def main():
    filepath = input("Enter path to Rosalind dataset:\n")
    trie = make_trie(filepath)
    tuples = trie.root.children_values()

    with open("output_solution.txt", "w") as output:
        for x in tuples:
            output.write("{0}\n".format(" ".join(x)))

if __name__ == "__main__":
    main()
