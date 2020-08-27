#! /usr/bin/env python3
'''
Calculate all possible subsets of maximum length n
'''

def main():
    total_subsets = 0
    N = int(input("Enter maximum set length:\n"))
    possible_subsets = 2**N
    print(possible_subsets % 1000000)

if __name__ == "__main__":
    main()
