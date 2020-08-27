#! /usr/bin/env python3

# Load in the data
with open("dataset.txt", "r") as data:
    n = int(data.readline().strip())
    string = data.readline().strip()
    A = list(map(float, data.readline().strip().split()))

## n = length of random DNA string
## string = Query string
## A = array of GC_content values

### Goal: Calculate the expected number of times, in each GC_content scenario [A], that 'string' will appear in a random DNA string of length 'n'
B = []
for GC_prob in A:
    AT = 0
    GC = 0
    for nuc in string:
        if nuc == "A" or nuc == "T":
            AT += 1
        else:
            GC += 1

    prob_of_string = (((1-GC_prob)/2) ** AT) * (((GC_prob)/2) ** GC)

    # Number of Sliding windows = length of genome - (length of substring - 1)
    sliding_windows = n - (len(string) - 1)

    B.append('%0.3f' % (prob_of_string * sliding_windows))

print(" ".join(B))
