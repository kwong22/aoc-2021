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

def read_cucumbers(lines):
    grid = []
    east = []
    south = []

    for line in lines:
        grid.append([c for c in line])

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '>':
                east.append([i, j])
            elif lines[i][j] == 'v':
                south.append([i, j])

    return grid, east, south

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def step(grid, east, south):
    num_moves = 0

    # East-facing herd moves first
    east_updates = {}

    # Determine valid moves
    for n in range(len(east)):
        i, j = east[n]
        next_i = i
        next_j = (j + 1) % len(grid[0])
        if grid[next_i][next_j] == '.':
            east_updates[(i, j)] = [n, next_i, next_j]

    # Update positions
    for i, j in east_updates.keys():
        grid[i][j] = '.'
        n, next_i, next_j = east_updates[(i, j)]
        grid[next_i][next_j] = '>'
        east[n] = [next_i, next_j]
        num_moves += 1

    # South-facing heard moves second
    south_updates = {}

    # Determine valid moves
    for n in range(len(south)):
        i, j = south[n]
        next_i = (i + 1) % len(grid)
        next_j = j
        if grid[next_i][next_j] == '.':
            south_updates[(i, j)] = [n, next_i, next_j]

    # Update positions
    for i, j in south_updates.keys():
        grid[i][j] = '.'
        n, next_i, next_j = south_updates[(i, j)]
        grid[next_i][next_j] = 'v'
        south[n] = [next_i, next_j]
        num_moves += 1

    return grid, east, south, num_moves

if __name__ == '__main__':
    lines = read_lines_from_file('input')
    grid, east, south = read_cucumbers(lines)
    num_steps = 500
    for i in range(num_steps):
        grid, east, south, num_moves = step(grid, east, south)
        if num_moves == 0:
            print(i + 1)
            break
