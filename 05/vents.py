#!/usr/bin/python

import re

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

def read_coords_from_line(line):
    coords = re.search(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups()
    return [int(x) for x in coords]

def read_vents_from_lines(lines):
    vents = []

    for line in lines:
        vents.append(read_coords_from_line(line))

    return vents

def map_vents(vents):
    max_x = 1000
    max_y = 1000

    # Create temp map
    temp_map = []
    for _ in range(max_y):
        temp_map.append([0] * max_x)

    for vent in vents:
        x1, y1, x2, y2 = vent

        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                temp_map[i][x1] += 1
        elif y1 == y2:
            for j in range(min(x1, x2), max(x1, x2) + 1):
                temp_map[y1][j] += 1
        else:
            # Diagonal line at exactly 45 degrees
            dx = (x2 - x1) // abs(x2 - x1)
            dy = (y2 - y1) // abs(y2 - y1)
            num_steps = abs(x2 - x1) + 1
            for i in range(num_steps):
                temp_map[y1 + dy * i][x1 + dx * i] += 1

    count = 0

    for i in range(max_y):
        for j in range(max_x):
            if temp_map[i][j] >= 2:
                count += 1

    return count

if __name__ == '__main__':
    vents = read_vents_from_lines(read_lines_from_file('input'))
    print(map_vents(vents))
