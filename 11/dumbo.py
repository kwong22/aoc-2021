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

def read_matrix_from_lines(lines):
    output = []
    for line in lines:
        output.append([int(c) for c in line])
    return output

def flash(i, j, matrix):
    height = len(matrix)
    width = len(matrix[0])

    for n in range(i - 1, i + 2):
        for m in range(j - 1, j + 2):
            if n >= 0 and n < height and m >= 0 and m < width:
                matrix[n][m] += 1

def check_for_flashes(matrix, flashed):
    height = len(matrix)
    width = len(matrix[0])

    need_update = False # True if flash occurred and need update

    num_flashes = 0

    while True:
        for i in range(height):
            for j in range(width):
                if matrix[i][j] > 9 and flashed[i][j] == 0:
                    # Flash only if has not yet flashed this step
                    flash(i, j, matrix)
                    flashed[i][j] = 1
                    num_flashes += 1
                    need_update = True
                else:
                    if i == height - 1 and j == width - 1:
                        # If end is reached and nothing to update, then return
                        if not need_update:
                            return num_flashes
                        else:
                            need_update = False

def step(matrix):
    # Matrix passed by reference
    height = len(matrix)
    width = len(matrix[0])

    flashed = [] # Track which indices have flashed this step
    for _ in range(height):
        flashed.append([0] * width)

    # Increase energy level by 1
    for i in range(height):
        for j in range(width):
            matrix[i][j] += 1

    num_flashes = check_for_flashes(matrix, flashed)

    # All indices that have flashed this step now have 0 energy
    for i in range(height):
        for j in range(width):
            if flashed[i][j] == 1:
                matrix[i][j] = 0

    return num_flashes

def step_n(matrix, n):
    total_flashes = 0

    for i in range(n):
        num_flashes = step(matrix)
        if num_flashes == len(matrix) * len(matrix[0]):
            print('All flashed on step {}'.format(i + 1))

        total_flashes += num_flashes

    return total_flashes

if __name__ == '__main__':
    matrix = read_matrix_from_lines(read_lines_from_file('input'))
    print(step_n(matrix, 500))

