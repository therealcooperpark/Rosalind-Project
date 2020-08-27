#! /usr/bin/env python3
'''
Perform basic set operations on given sets from a file
'''


def parse_file(filepath):
    with open(filepath, "r") as file:
        # Read in the integer, create a set of n values
        n = int(file.readline().strip())
        setN = set([x for x in range(1,n+1)])

        # Read in each set. File formatting requires overhaul to be python set
        setA = file.readline().strip()[1:-1].split(", ")
        setA = set([int(x) for x in setA])

        setB = file.readline().strip()[1:-1].split(", ")
        setB = set([int(x) for x in setB])
    return setN, setA, setB


def write_file(setN, setA, setB):
    '''
    Write out A union B,
    A intersection B
    A difference B
    B difference A
    N difference A
    N difference B
    '''
    with open("output_solution.txt", "w") as output:
        output.write("{0}\n".format(str(setA.union(setB))))
        output.write("{0}\n".format(str(setA.intersection(setB))))
        output.write("{0}\n".format(str(setA.difference(setB))))
        output.write("{0}\n".format(str(setB.difference(setA))))
        output.write("{0}\n".format(str(setN.difference(setA))))
        output.write("{0}\n".format(str(setN.difference(setB))))


def main():
    filepath = input("Enter dataset filepath:\n")
    setN, setA, setB = parse_file(filepath)
    write_file(setN, setA, setB)


if __name__ == "__main__":
    main()
