def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    # s = ['a', 'b', 'c]
    # [False, False, False, True]
    # Looping from the end, at each index, test the substring from the index until the length of the word
    # being tested. If it's match, take the value just after the length of the substring and copy if over.
    # Repeat for every index. Once we get to the very first index and test it, the resulting value will
    # be our final value.
    dp = [False for _ in range(len(s) + 1)]
    dp[len(s)] = True
    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if (i + len(word)) <= len(s) and s[i:i + len(word)] == word:
                dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
    return dp[0]


input = 'abcd'
words = ["a", "abc", "b", "cd"]
res = wordBreak(input, words)
print(res)
