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

def count_increases_window(depths, win_size=3):
    """Counts number of increases between consecutive windows of certain size.

    Args:
        depths: list of integers representing depths
        win_size: number of integers per window
    Returns:
        Number of increases between consecutive windows
    """
    if len(depths) < win_size + 1:
        return 0

    num_increases = 0

    for i in range(win_size, len(depths)):
        if depths[i] > depths[i - win_size]:
            num_increases += 1

    return num_increases

if __name__ == '__main__':
    lines = read_lines_from_file('input')
    ints = [int(line) for line in lines]
    print(count_increases_window(ints))
