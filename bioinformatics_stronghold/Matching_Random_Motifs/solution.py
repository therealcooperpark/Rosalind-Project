#! /usr/bin/env python3

# Read in data
with open("dataset.txt", "r") as file:
    nums = file.readline()
    nums = nums.strip().split()
    rand_str, GC_prob = int(nums[0]),float(nums[1])
    match = file.readline()
    match = match.strip()

AT = 0
GC = 0

# Identify probability of nucleotide
for nuc in match:
    if nuc == "A" or nuc == "T":
        AT += 1
    else:
        GC += 1


# Formula = (((Probability of A/T) / 2) ^ #of A/T) * (((Probability of G/C) / 2) ^ #of G/C)
prob_of_string = (((1- GC_prob)/2) ** AT) * (((GC_prob)/2) ** GC)

# Formula = 1 - [1 - prob_of_string]^(# of strings)
total_prob = 1 - (1 - prob_of_string) ** rand_str

print('%0.3f' % total_prob)
