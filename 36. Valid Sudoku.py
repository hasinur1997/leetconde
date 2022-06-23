# Problem Link https://leetcode.com/problems/valid-sudoku/

def is_valid_sudoku(board):
    new_board = list(map(list, zip(*board)))
    digits = [i for i in range(1, 10)]
    for row in board:
        if len(set(row)) != len(row):
            return False

    for row in new_board:
        if len(set(row)) != len(row):
            return False

    return True


# digits = [i for i in range(1, 10)]
#
# print(digits)