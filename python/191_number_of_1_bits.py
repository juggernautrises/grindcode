# https://leetcode.com/problems/number-of-1-bits/
def hammingWeight(n):
    ones = 0
    while n > 0:
        if n % 2:
            ones += 1
    return ones


n = 11
res = hammingWeight(n)
print(res)
