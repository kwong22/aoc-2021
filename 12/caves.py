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

def read_graph_from_lines(lines):
    graph = {}

    def add_to_dict(key, val, d):
        if key in d:
            d[key].append(val)
        else:
            d[key] = [val]

    for line in lines:
        a, b = line.split('-')
        if a != 'end' and b != 'start':
            add_to_dict(a, b, graph)
        if b != 'end' and a != 'start':
            add_to_dict(b, a, graph)

    return graph

def count_paths(graph):

    def dfs(cave, graph, visited):
        if cave == 'end':
            return 1

        if cave in visited:
            if cave.islower():
                return 0
        else:
            visited.append(cave)

        num_paths = 0

        for next_cave in graph[cave]:
            num_paths += dfs(next_cave, graph, visited[:])

        return num_paths

    return dfs('start', graph, [])

def count_paths2(graph):

    def dfs(cave, graph, visited, visited_twice):
        if cave == 'end':
            return 1

        if cave in visited:
            if cave.islower():
                if visited_twice:
                    return 0
                else:
                    visited_twice = True
        else:
            visited.append(cave)

        num_paths = 0

        for next_cave in graph[cave]:
            num_paths += dfs(next_cave, graph, visited[:], visited_twice)

        return num_paths

    return dfs('start', graph, [], False)

if __name__ == '__main__':
    graph = read_graph_from_lines(read_lines_from_file('input'))
    print(count_paths(graph))
    print(count_paths2(graph))
