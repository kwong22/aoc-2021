#!/usr/bin/python

def read_lines_from_file(fname):
    """Builds list of strings line-by-line from a file.

    Args:
        fname: name of file to read from
    Returns:
        List of strings
    """
    output = []
    with open(fname, 'r') as lines:
        for line in lines:
            line = line.strip()
            output.append(line)
    return output

def read_ints_from_line(line):
    return [int(x) for x in line.split(',')]

def align_crabs(crabs):
    min_x = min(crabs)
    max_x = max(crabs)

    min_fuel = len(crabs) * max_x * (max_x + 1) / 2

    for i in range(min_x, max_x + 1):
        fuel = 0
        for x in crabs:
            #fuel += abs(x - i)
            fuel += abs(x - i) * (abs(x - i) + 1) / 2

        min_fuel = min(fuel, min_fuel)

    return min_fuel

if __name__ == '__main__':
    crabs = read_ints_from_line(read_lines_from_file('input')[0])
    print(align_crabs(crabs))
