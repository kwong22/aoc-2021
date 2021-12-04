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

def read_board_from_lines(lines):
    board = []

    for line in lines:
        row = []
        for x in line.split():
            row.append(int(x))
        board.append(row)

    return board

def read_bingo_input(fname):
    lines = read_lines_from_file(fname)
    nums_drawn = [int(x) for x in lines[0].split(',')]
    boards = []

    # Read boards
    i = 1
    while i < len(lines):
        boards.append(read_board_from_lines(lines[i + 1:i + 6]))
        i += 6

    return nums_drawn, boards

def check_board_for_win(board):
    """Checks Bingo board for completed row or column.

    Args:
        board: list of equal-length lists representing a board, values 0 or 1
    Returns:
        Boolean indicating whether the board has a completed row or column
        (containing all 1s)
    """
    num_rows = len(board)
    num_cols = len(board[0]) # Assume all rows have equal number of columns

    # Check rows
    for i in range(num_rows):
        for j in range(num_cols):
            if board[i][j] == 0:
                break # Stop looking in this row
            if j == num_cols - 1:
                return True # Reached end of row, all 1s

    # Check columns
    for j in range(num_cols):
        for i in range(num_rows):
            if board[i][j] == 0:
                break # Stop looking in this column
            if i == num_rows - 1:
                return True # Reached end of column, all 1s

    return False

def compute_winning_board(nums_drawn, boards):
    num_rows = len(boards[0])
    num_cols = len(boards[0][0])

    # Create temporary boards
    temp_boards = []
    for _ in range(len(boards)):
        curr_board = []
        for _ in range(num_rows):
            curr_board.append([0] * num_cols)
        temp_boards.append(curr_board)

    # Go through drawn numbers and find winning board
    for x in nums_drawn:
        for b in range(len(boards)):
            for i in range(num_rows):
                for j in range(num_cols):
                    if boards[b][i][j] == x:
                        temp_boards[b][i][j] = 1

            if check_board_for_win(temp_boards[b]):
                # Calculate final score (sum of unmarked numbers * number drawn)
                unmark_sum = 0
                for i in range(num_rows):
                    for j in range(num_cols):
                        if temp_boards[b][i][j] == 0:
                            unmark_sum += boards[b][i][j]
                return unmark_sum * x

    return -1

def compute_last_winning_board(nums_drawn, boards):
    num_rows = len(boards[0])
    num_cols = len(boards[0][0])

    # Create temporary boards
    temp_boards = []
    for _ in range(len(boards)):
        curr_board = []
        for _ in range(num_rows):
            curr_board.append([0] * num_cols)
        temp_boards.append(curr_board)

    # Track remaining boards
    remaining_boards = [1] * len(boards)

    # Go through drawn numbers and find winning board
    for x in nums_drawn:
        for b in [i for i, val in enumerate(remaining_boards) if val == 1]:
            for i in range(num_rows):
                for j in range(num_cols):
                    if boards[b][i][j] == x:
                        temp_boards[b][i][j] = 1

            if check_board_for_win(temp_boards[b]):
                if sum(remaining_boards) > 1:
                    remaining_boards[b] = 0
                else:
                    # Calculate final score (sum of unmarked numbers * number drawn)
                    unmark_sum = 0
                    for i in range(num_rows):
                        for j in range(num_cols):
                            if temp_boards[b][i][j] == 0:
                                unmark_sum += boards[b][i][j]
                    return unmark_sum * x

    return -1

if __name__ == '__main__':
    nums_drawn, boards = read_bingo_input('input')
    print('Score of first winning board:',
            compute_winning_board(nums_drawn, boards))
    print('Score of last winning board:',
            compute_last_winning_board(nums_drawn, boards))

