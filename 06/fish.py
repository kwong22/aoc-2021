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

def read_fish_from_line(line):
    return [int(x) for x in line.split(',')]

def simulate_fish(fish, num_days):
    """Simulate fish

    Args:
        fish: List of integers representing number of days until reproduction
    Returns:
        Number of fish
    """
    temp = fish.copy()

    for _ in range(num_days):
        temp_add = []
        for i in range(len(temp)):
            if temp[i] > 0:
                temp[i] -= 1
            else:
                temp[i] = 6
                temp_add.append(8)
        temp += temp_add

    return len(temp)

def simulate_fish2(fish, num_days):
    fish_by_day = [0] * 9
    for f in fish:
        fish_by_day[f] += 1

    for _ in range(num_days):
        new_fish = fish_by_day[0]
        for i in range(8):
            fish_by_day[i] = fish_by_day[i + 1]
        fish_by_day[6] += new_fish
        fish_by_day[8] = new_fish

    return sum(fish_by_day)

if __name__ == '__main__':
    fish = read_fish_from_line(read_lines_from_file('input')[0])
    print(simulate_fish(fish, 80))
    print(simulate_fish2(fish, 80))
    print(simulate_fish2(fish, 256))
