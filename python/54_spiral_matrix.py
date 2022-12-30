# https://leetcode.com/problems/spiral-matrix/

def spiralOrder(matrix):
    res = []

    ROWS = len(matrix)
    COLS = len(matrix[0])
    l = 0
    r = COLS
    top = 0
    bottom = ROWS
    # Start with the left and right for the columns and top and bottom for the rows
    while l < r and top < bottom:
        # Get the numbers in the top row
        for i in range(l, r):
            res.append(matrix[top][i])

        # Move the top row down
        top += 1

        # Get right side column
        for i in range(top, bottom):
            res.append(matrix[i][r - 1])

        # Move the column in
        r -= 1

        # Check if the left and right and top and bottom have not yet touched or crossed
        if not (l < r and top < bottom):
            return res

        # Add the bottom number, from the end until the start
        for i in range(r - 1, l - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        # Add the left side numbers from the bottom going up
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][l])
        l += 1
    return res
