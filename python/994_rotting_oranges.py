# https://leetcode.com/problems/rotting-oranges/
import collections
# Find all the fresh oranges and add all the rotten oranges to the queue
# Do a BFS search on the rotting oranges queue and increase the number of minutes by one on each
# iteration and decrease the number of fresh oranges every time the orange is

def orangesRotting(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    q = collections.deque()
    minutes = 0
    fresh_oranges = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh_oranges += 1
            if grid[r][c] == 2:
                q.append((r, c))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while q and fresh_oranges > 0:
        len_q = len(q)
        for i in range(len_q):
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != 1):
                    continue
                grid[row][col] = 2
                q.append((row, col))
                fresh_oranges -= 1
        minutes += 1
    return minutes if fresh_oranges == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

res = orangesRotting(grid)
print(res)
