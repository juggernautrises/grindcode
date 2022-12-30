# https://leetcode.com/problems/rotate-image/
# Create four pointers: top and bottom for the rows and left and right for the columns.
# Store the top left value, and copy the values from the corresponding location in a counter clockwise manner.
# Do this for every column between l and r.

def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    l = 0
    r = len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top = l
            bottom = r

            top_left = matrix[top][l + i]
            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = top_left
        l += 1
        r -= 1
