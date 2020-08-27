#! /usr/bin/env python3


def longestsubstr(collection, length):
    ### Longest increasing
    # Follow the path of longest increasing substring
    m_references = {}
    d_references = {}

    # Recreate the list with 1s (increasing) and max value (decreasing)
    m_idxls = [1 for _ in range(len(collection))]
    d_idxls = [1 for _ in range(len(collection))]

    # Iterate over collection and mark increasing substrings
    for i in range(len(collection)):
        for j in range(i + 1, len(collection)):
            # Increasing
            if collection[i] < collection[j] and m_idxls[i] + 1 > m_idxls[j]:
                m_idxls[j] = m_idxls[i] + 1
                m_references[j] = i

            # Decreasing
            if collection[i] > collection[j] and d_idxls[i] + 1 > d_idxls[j]:
                d_idxls[j] = d_idxls[i] + 1
                d_references[j] = i

    print("Longest increasing: {0}\nLongest decreasing: {1}".format(max(m_idxls), max(d_idxls)))
    # Get max length of list
    m_listpointer = m_idxls.index(max(m_idxls))
    d_listpointer = d_idxls.index(max(d_idxls))

    # Get longest increasing substring
    longest_increase = [collection[m_listpointer]]
    for _ in range(max(m_idxls) - 1):
        longest_increase.insert(0,collection[m_references[m_listpointer]])
        m_listpointer = m_references[m_listpointer]

    # Get longest decreasing substring
    longest_decrease = [collection[d_listpointer]]
    for _ in range(max(d_idxls) - 1):
        longest_decrease.insert(0,collection[d_references[d_listpointer]])
        d_listpointer = d_references[d_listpointer]

    return([longest_increase,longest_decrease])

# Get the data
with open("dataset.txt", "r") as input:
    length = input.readline()
    length = int(length.strip())
    dataset = []
    data = input.readline()
    data = data.strip().split()
    for num in data:
        dataset.append(int(num))

print("Length of list {0}\nNumber: {1}".format(len(dataset), length))

longests = longestsubstr(dataset, length)

with open("longest.txt", "w") as output:
    for string in longests:
        string = " ".join(list(map(str, string)))
        output.write("{0}\n".format(string))
