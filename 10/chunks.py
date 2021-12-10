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

def score_corrupted_lines(lines):
    total_score = 0

    open_chars = ['(', '[', '{', '<']

    close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{',
            '>': '<'
            }

    char_to_score = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
            }

    for line in lines:
        char_buff = []
        for c in line:
            if c in open_chars:
                char_buff.append(c)
            else:
                if close_to_open[c] == char_buff[-1]:
                    char_buff.pop()
                else:
                    total_score += char_to_score[c]
                    break

    return total_score

def autocomplete_lines(lines):
    open_chars = ['(', '[', '{', '<']

    close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{',
            '>': '<'
            }

    open_to_close = {val: key for key, val in close_to_open.items()}

    char_to_score = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4
            }

    all_scores = []

    for line in lines:
        char_buff = []
        corrupted = False
        for c in line:
            if c in open_chars:
                char_buff.append(c)
            else:
                if close_to_open[c] == char_buff[-1]:
                    char_buff.pop()
                else:
                    # This line is corrupted
                    corrupted = True
                    break

        if corrupted:
            # Do not compute score for corrupted lines
            continue

        # Complete the line
        line_score = 0
        while char_buff:
            line_score  = line_score * 5 + char_to_score[open_to_close[char_buff[-1]]]
            char_buff.pop()
        all_scores.append(line_score)

    all_scores.sort()
    return all_scores[len(all_scores) // 2]

if __name__ == '__main__':
    lines = read_lines_from_file('input')
    print(score_corrupted_lines(lines))
    print(autocomplete_lines(lines))
