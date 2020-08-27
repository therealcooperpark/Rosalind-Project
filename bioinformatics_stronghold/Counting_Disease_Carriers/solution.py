#! /usr/bin/env python3
'''
Calculate the probability of an individual having at least one copy of the recessive trait
Given the proportion of a population in genetic equilibrium
'''
import math

def parse_file(filepath):
    # Return list of floats from file
    with open(filepath, "r") as file:
        return [float(x) for x in file.readline().strip().split()]


def recessive_probability(pop_list):
    # For each population and assuming genetic equilibrium...
    # Calculate the probability of the recessive trait being present
    prob_list = []
    for population in pop_list:
        #p**2 + 2*p*q + q**2 = 1, solve for p
        q = math.sqrt(population)
        p = quadratic(1, 2*q, -1+population)
        prob_list.append(2*p*q + population)
    return prob_list


def quadratic(a, b, c):
    # Solve quadratic formula, return real positive number
    discriminant = b**2-4*a*c

    if discriminant == 0:
        x = (-b + math.sqrt(discriminant)) / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b + math.sqrt(discriminant)) / (2*a)
        if x1 > 0:
            return x1
        else:
            return x2


def write_output(prob_list):
    # Write output in single line to file
    with open("answer.txt", "w") as output:
        output.write(" ".join([str(x) for x in prob_list]))


def main():
    filepath = input("Enter filepath to input data:\n")
    pop_list = parse_file(filepath)
    prob_list = recessive_probability(pop_list)
    write_output(prob_list)

if __name__ == "__main__":
    main()
