def longestCommonSubsequence(text1, text2):
    # Set up a 2D array where the size of each row is one more than the length
    # of the first string and the column is one more than the length of the second
    dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    # For every index starting at 1 (we offset when we check the actual string)
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            # Check if the character at index-1 (for the offset) matches. If it does
            # take the value of the dp array just behind and above and +1 and add it to the
            # dp array at the current indices
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            # If it doesn't match, get the max of the value just behind or just above
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # Return the last element of the last row
    return dp[-1][-1]


a = 'bl'
b = 'yby'

res = longestCommonSubsequence(a, b)
print(res)

