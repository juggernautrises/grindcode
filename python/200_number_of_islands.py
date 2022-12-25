# https://leetcode.com/problems/number-of-islands/submissions/859387113/

import collections

# Iterate through each position in the grid. If we encounter a 1 and the position hasn't been visited, we perform a
# BFS on that position. This BFS will continue until there are no more connected ones to traverse and at that point
# we increment our 'islands' count by one.
# IMPORTANT NOTE TO SELF: Mark a position as visited at the same time you add it to a queue!

def numIslands(grid):
    visited = set()
    islands = 0
    ROWS = len(grid)
    COLS = len(grid[0])

    def bfs(row, col):
        q = collections.deque()
        visited.add((row, col))
        q.append((row, col))
        while q:
            row, col = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r = row + dr
                c = col + dc
                if r in range(ROWS) and c in range(COLS) and (r, c) not in visited and grid[r][c] == '1':
                    q.append((r, c))
                    visited.add((r, c))

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == '1' and (row, col) not in visited:
                bfs(row, col)
                islands += 1
    return islands
