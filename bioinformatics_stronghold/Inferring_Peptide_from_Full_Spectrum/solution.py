#! /usr/bin/env python3
'''
Infer one possible protein sequence given a list of b- and y-ions
and the total parent weight.
'''

def parse_file(filepath):
    '''
    Parse file, giving back parent weight and list of ion weights
    paired against the total parent value
    '''

    with open(filepath, "r") as file:
        parent_weight = float(file.readline().strip())
        ions = []
        for line in file:
            ions.append(float(line.strip()))

    # Pair the ions
    ion_pairs = []
    for i in range( int(len(ions)/2) ):
        ion_pairs.append( (ions[i], ions[-i - 1]) )
    return parent_weight, ion_pairs


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


def within_num(x, y, num):
    '''
    Find if "x" is within "num" of "y"
    '''

    if x > y - num and x < y + num:
        return True
    else:
        return False


def check_ion_order(ion_pairs, valid_weights):
    '''
    Rearrange ion pairs so all b- ions are in the correct order
    '''

    idx = 0
    while idx < len(ion_pairs) - 1:
        # Calculate weight difference, see if it matches an isotope value
        weight_dif = ion_pairs[idx + 1][0] - ion_pairs[idx][0]
        valid = [1 for weight in valid_weights if within_num(weight_dif, weight, 0.001)]
        if len(valid) == 0:
            # If not, rearrange the pair and update list, resort it.
            changing = ion_pairs[idx + 1]
            ion_pairs[idx + 1] = (changing[1], changing[0])
            ion_pairs = sorted(ion_pairs, key = lambda x: x[0])
        else:
            idx += 1
    return ion_pairs


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


def main():
    filepath = input("Enter path to data file:\n")
    parent_weight, ion_pairs = parse_file(filepath)
    iso_table = get_iso_table()
    new_ion_order = check_ion_order(ion_pairs, [x[1] for x in iso_table])
    b_ions = [x[0] for x in new_ion_order]
    protein = spectrum_to_protein(b_ions, iso_table)
    print(protein)


if __name__ == "__main__":
    main()
