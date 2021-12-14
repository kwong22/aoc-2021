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

def print_coords(coords):
    max_x = max([x for x, y in coords])
    max_y = max([y for x, y in coords])

    for y in range(max_y + 1): # Add 1
        for x in range(max_x + 1): # Add 1
            if (x, y) in coords:
                print('#', end='')
            else:
                print('.', end='')
        print('')

def fold(lines):
    coords = []
    folds = []

    i = 0
    while lines[i]:
        a, b = lines[i].split(',')
        coords.append((int(a), int(b)))
        i += 1

    i += 1

    while i < len(lines):
        d, n = lines[i].split()[-1].split('=')
        folds.append((d, int(n)))
        i += 1

    def fold_helper(coords, direction, amt):
        idx_to_change = 0
        if direction == 'y':
            idx_to_change = 1

        new_coords = []

        for coord in coords:
            new_coord = [0, 0]
            other_idx = (idx_to_change + 1) % 2
            new_coord[other_idx] = coord[other_idx]
            if coord[idx_to_change] > amt:
                new_coord[idx_to_change] = 2 * amt - coord[idx_to_change]
            else:
                new_coord[idx_to_change] = coord[idx_to_change]

            new_coord = (new_coord[0], new_coord[1])
            if new_coord not in new_coords:
                new_coords.append(new_coord)

        return new_coords

    for fold in folds:
        coords = fold_helper(coords, fold[0], fold[1])

    return coords

if __name__ == '__main__':
    lines = read_lines_from_file('input')
    coords = fold(lines)
    print_coords(coords)
