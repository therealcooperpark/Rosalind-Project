#! /usr/bin/env python3

####
# Solution: You need to track all unique spots for 0.
#           Your script currently eats all 0s into a single spot in the dictionary
#           Check for multiple zeroes and you can save a bunch of headache for that
#           list.



'''
Find two indicies where 
list[idx1] == -list[idx2]
Return -1 if not found
'''

from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument('input', help = 'input file from Rosalind')
    parser.add_argument('output', help = 'output file name')
    return parser.parse_args()


def parse_input(input_file):
    '''
    Parse input file to get all lists to test
    '''

    lists = []
    with open(input_file, 'r') as file:
        next(file)  # Skip stats line
        for line in file:
            # Turn line into list of integers
            array = [int(x) for x in line.strip().split()]
            # 
            array_dict = {}
            for idx,num in enumerate(array):
                if num == 0:
                    array_dict.setdefault(0, [])
                    array_dict[0].append(idx)
                else:
                    array_dict[num] = idx

            lists.append( (array_dict) )
    return lists


def write_output(lists, output_name):
    '''
    Find correct indicies and write to output file
    '''

    with open(output_name, 'w') as output:
        # For each value in each array,
        # Try to pull it's inverse value from the dict of known values
        for array in lists:
            for num in array:
                opposite = False
                try:
                    opp_num = num * -1
                    opposite = array[num*-1]
                    break
                except KeyError:
                    continue

            # If the inverse value exists, log the two indicies
            if opposite:
                print(num, opp_num, opposite)
                if isinstance(opposite, list):
                    # If the values were 0, log it this way
                    if len(opposite) > 1:
                        output.write('{0} {1}\n'.format(opposite[0]+1, opposite[1]+1))
                    else:
                        output.write('-1\n')
                # If the values were x & -x, log it this way
                elif array[num] < opposite:
                    output.write('{0} {1}\n'.format(array[num]+1, opposite+1))
                else:
                    output.write('{0} {1}\n'.format(opposite+1, array[num]+1))
            else:
                output.write('-1\n')


def main():
    args = get_args()
    lists = parse_input(args.input)
    write_output(lists, args.output)


if __name__ == '__main__':
    main()
