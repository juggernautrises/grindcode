# https://leetcode.com/problems/word-search/
# For every cell in the board, we are going to perform a DFS on it. To do this we:
# 1) Check if the provided row and column is in bounds and that the character at the given point is equal to the
#    character in the word at the provided word's index.
# 2) If the above is true, we can temporarily mark the grid as visited and then call the DFS function on the relevant
#    surrounding cells.
# 3) After DFS is called on all these, we have to remember to unmark the cell.

def exist(board, word):
    ROWS = len(board)
    COLS = len(board[0])

    def check(row, col, word_index):
        if word_index == len(word):
            return True
        if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] != word[word_index]:
            return False
        board[row][col] = '#'
        res = (
                check(row + 1, col, word_index + 1) or
                check(row - 1, col, word_index + 1) or
                check(row, col + 1, word_index + 1) or
                check(row, col - 1, word_index + 1))
        board[row][col] = word[word_index]
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if check(r, c, 0):
                return True
    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

print(exist(board, word))
