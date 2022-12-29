# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# Since the top and bottoms of the board both touch the pacific and atlantic, we'll perform a DFS on each of these cells
# and place the results in their own ocean specific set. We then perform the same with the left and ride sides of the
# grid. Once we complete these DFS searches, we just check to see what points exist in both sets.

def pacificAtlantic(heights):
    ROWS = len(heights)
    COLS = len(heights[0])

    pac = set()
    atl = set()

    def dfs(row, col, ocean_set, prev):
        if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                ((row, col) in ocean_set) or
                (heights[row][col] < prev)
        ):
            return
        ocean_set.add((row, col))
        dfs(row + 1, col, ocean_set, heights[row][col])
        dfs(row - 1, col, ocean_set, heights[row][col])
        dfs(row, col + 1, ocean_set, heights[row][col])
        dfs(row, col - 1, ocean_set, heights[row][col])

    for row in range(ROWS):
        dfs(row, 0, pac, heights[row][0])
        dfs(row, COLS - 1, atl, heights[row][COLS - 1])

    for col in range(COLS):
        dfs(0, col, pac, heights[0][col])
        dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])

    res = []
    for h in pac:
        if h in atl:
            res.append(h)
    return res
