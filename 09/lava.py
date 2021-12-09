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

def read_map_from_lines(lines):
    mat = []

    for line in lines:
        mat.append([int(x) for x in line])

    return mat

def is_low_point(i, j, mat):
    height = len(mat)
    width = len(mat[0])

    if i - 1 >= 0 and mat[i - 1][j] <= mat[i][j]:
        return False

    if i + 1 < height and mat[i + 1][j] <= mat[i][j]:
        return False

    if j - 1 >= 0 and mat[i][j - 1] <= mat[i][j]:
        return False

    if j + 1 < width and mat[i][j + 1] <= mat[i][j]:
        return False

    return True

def count_low_points(mat):
    result = 0
    height = len(mat)
    width = len(mat[0])

    for i in range(height):
        for j in range(width):
            if is_low_point(i, j, mat):
                result += 1 + mat[i][j]

    return result

def find_basins(mat):
    basin_sizes = []
    height = len(mat)
    width = len(mat[0])

    # Track locations that have been visited
    visited = []
    for _ in range(height):
        visited.append([0] * width)

    def dfs(i, j, visited, mat):
        height = len(mat)
        width = len(mat[0])

        # Check within bounds
        if i < 0 or i >= height or j < 0 or j >= width:
            return 0

        # Check visited status (visited is passed by reference)
        if visited[i][j] == 1:
            return 0

        visited[i][j] = 1

        # Check within basin
        if mat[i][j] == 9:
            return 0

        # Add to basin
        size = 1

        # Explore basin
        size += dfs(i - 1, j, visited, mat)
        size += dfs(i + 1, j, visited, mat)
        size += dfs(i, j - 1, visited, mat)
        size += dfs(i, j + 1, visited, mat)

        return size

    for i in range(height):
        for j in range(width):
            if visited[i][j] == 1:
                continue

            if mat[i][j] == 9:
                continue
            else:
                basin_sizes.append(dfs(i, j, visited, mat))

            visited[i][j] = 1

    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

if __name__ == '__main__':
    mat = read_map_from_lines(read_lines_from_file('input'))
    print(count_low_points(mat))
    print(find_basins(mat))
