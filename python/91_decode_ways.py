# https://leetcode.com/problems/decode-ways/

def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    # The general idea is that if we have a valid single digit, we need to copy the number of combinations from the
    # previous digit (since we are only adding another number to the previous set of combinations). If a single
    # digit is 0, the number of combinations at that point will just be 0. We then need to add the number of
    # combinations using a valid two digit sequence from just before the start of the two digit sequence.

    dp = [0 for _ in range(len(s))]
    dp[0] = 1 if s[0] != 0 else 0
    if len(s) == 1:
        return dp[0]

    if s[1] == '0':
        dp[1] = 0
    else:
        dp[1] = dp[0]
    if s[0] == '1' or (s[0] == '2' and s[1] in '0123456'):
        dp[1] += 1

    for i in range(2, len(s)):
        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i - 1]

        if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] in '0123456'):
            dp[i] += dp[i - 2]
    return dp[-1]


s = '10'
res = numDecodings(s)
print(res)
