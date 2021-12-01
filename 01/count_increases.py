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

def read_ints_from_file(fname):
    lines = read_lines_from_file(fname)
    return [int(line) for line in lines]

def count_increases(depths):
    """Counts number of increases between consecutive integers.

    Args:
        depths: list of integers representing depths
    Returns:
        Number of increases between consecutive integers
    """
    if len(depths) < 2:
        return 0

    num_increases = 0

    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            num_increases += 1

    return num_increases

if __name__ == '__main__':
    print(count_increases(read_ints_from_file('input')))
