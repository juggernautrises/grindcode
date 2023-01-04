# https://leetcode.com/problems/valid-sudoku/
import collections
# Go through every cell in the grid. Add it to a set for the row, column, and subgrid. If it already
# exists in any of those sets, we can return False.

def isValidSudoku(board):
    row_set = collections.defaultdict(set)
    col_set = collections.defaultdict(set)
    grid_set = collections.defaultdict(set)
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == '.':
                continue
            num = board[row][col]
            grid = (row // 3, col // 3)
            if num in row_set[row] or num in col_set[col] or num in grid_set[grid]:
                return False
            row_set[row].add(num)
            col_set[col].add(num)
            grid_set[grid].add(num)
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
res = isValidSudoku(board)
print(res)
