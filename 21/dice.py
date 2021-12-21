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

def play_game(lines):
    num_players = len(lines)
    positions = [0] * num_players
    for i in range(num_players):
        positions[i] = int(lines[i].split()[-1]) - 1
    max_position = 10

    scores = [0] * num_players
    max_score = 1000

    die = 0 # one less to be able to use modulo
    max_die = 100
    num_rolls = 3
    total_num_rolls = 0

    curr_player = 0

    while sum([score >= max_score for score in scores]) == 0:
        for _ in range(num_rolls):
            positions[curr_player] = (positions[curr_player] + die + 1) % max_position
            total_num_rolls += 1
            die = (die + 1) % max_die
        scores[curr_player] += positions[curr_player] + 1
        curr_player = (curr_player + 1) % num_players

    return min(scores) * total_num_rolls

if __name__ == '__main__':
    lines = read_lines_from_file('input')
    print(play_game(lines))

    test_input = [
            'Player 1 starting position: 4',
            'Player 2 starting position: 8'
            ]
    print(play_game(test_input))
