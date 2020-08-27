#! /usr/bin/env python3
'''
Infer a protein string based on a list of prefix specturm values
'''

def parse_file(filepath):
    '''
    Parse spectrum file into sorted list
    '''

    spectrum_list = []
    with open(filepath, "r") as file:
        for line in file:
            # Append spectrum value to list, rounding for consistency
            spectrum_list.append(round(float(line.strip()), 4))
    return spectrum_list


def get_iso_table():
    '''
    Load monoisotopic mass table from file into 2D list
    '''

    iso_table = []
    with open("monoisotopic_mass.txt", "r") as file:
        for line in file:
            line = line.split()
            iso_table.append( (line[0], float(line[1].strip())) )

    sorted_iso_table = sorted(iso_table, key=lambda x: x[1])
    return sorted_iso_table


def spectrum_to_protein(spectrum_list, iso_table):
    '''
    Take raw sorted spectrum values and extract individual
    Amino Acid weights. aa[i] = spectrum_list[i + 1] - spectrum_list[i]
    Convert weights to AA string
    '''

    # Get weights
    aa_weights = []
    for i in range(len(spectrum_list) - 1):
        aa_weights.append(spectrum_list[i+1] - spectrum_list[i])

    # Convert weights to string
    aa_string = ""
    for weight in aa_weights:
        idx = 0
        while not within_num(weight, iso_table[idx][1], 0.001):
            idx += 1
        aa_string += iso_table[idx][0]
    return aa_string


def within_num(x, y, num):
    '''
    Find if "x" is within "num" of "y"
    '''

    if x > y - num and x < y + num:
        return True
    else:
        return False


def main():
    filepath = input("Enter filepath to list of values:\n")
    spectrum_list = parse_file(filepath)
    iso_table = get_iso_table()
    print(iso_table)
    protein = spectrum_to_protein(spectrum_list, iso_table)
    print(protein)


if __name__ == "__main__":
    main()
