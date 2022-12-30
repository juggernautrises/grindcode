# https://leetcode.com/problems/unique-paths/
# The first row and first column will always be one since there is only one way to get to that position given the
# problem constraints. We can then begin at index 1 and column 1, and iterate through each cell and calculate the
# number of paths by looking them up in the DP array.


def uniquePaths(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for i in range(n):
        dp[0][i] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


m = 3
n = 7

res = uniquePaths(m, n)
print(res)
