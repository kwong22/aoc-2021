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

def pilot_sub(commands):
    """Compute final position of submarine from list of commands.

    Commands have the form '{direction} {distance}'
    where direction can take the form: 'up', 'down', 'forward'
    and distance is an integer.

    'up' decreases depth by distance.
    'down' increases depth by distance.
    'forward' increases horizontal position by distance.

    Args:
        commands: list of strings representing commands
    Returns:
        Tuple of (horizontal position, depth)
    """
    x = 0 # horizontal position
    y = 0 # depth

    for command in commands:
        direction, dist = command.split()

        if direction == 'forward':
            x += int(dist)
        elif direction == 'up':
            y -= int(dist)
        elif direction == 'down':
            y += int(dist)
        else:
            raise ValueError('Invalid value for direction: {}'.
                    format(direction))

    return x, y

def pilot_sub2(commands):
    """Compute final position of submarine from list of commands.

    In this second version, there is an additional value called 'aim'.

    Commands have the form '{direction} {distance}'
    where direction can take the form: 'up', 'down', 'forward'
    and distance is an integer.

    'up' decreases aim by distance.
    'down' increases aim by distance.
    'forward' increases horizontal position by distance and increases depth by
        aim * distance.

    Args:
        commands: list of strings representing commands
    Returns:
        Tuple of (horizontal position, depth)
    """
    x = 0 # horizontal position
    y = 0 # depth
    aim = 0

    for command in commands:
        direction, dist = command.split()

        if direction == 'forward':
            x += int(dist)
            y += aim * int(dist)
        elif direction == 'up':
            aim -= int(dist)
        elif direction == 'down':
            aim += int(dist)
        else:
            raise ValueError('Invalid value for direction: {}'.
                    format(direction))

    return x, y

if __name__ == '__main__':
    x, y = pilot_sub(read_lines_from_file('input'))
    print(x, y, x * y)
    x, y = pilot_sub2(read_lines_from_file('input'))
    print(x, y, x * y)
