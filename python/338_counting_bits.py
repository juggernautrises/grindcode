# https://leetcode.com/problems/counting-bits/description/
def countBits(n):
    ones = [0]
    for i in range(1, n + 1):
        ones.append(ones[i // 2] + i % 2)
    return ones
