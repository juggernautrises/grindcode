# https://leetcode.com/problems/longest-repeating-character-replacement/
# Create two pointers, r and l, where r will always move forward. As r moves forward, add it to a hashmap which keeps
# track of the character count. Get the length of the current substring and if the length exceeds the highest count in
# the hashmap then remove the l character and increase l. For each iteration, check the max length.

def characterReplacement(s, k):
    freq = {}
    l = 0
    res = 0
    for r in range(len(s)):
        freq[s[r]] = freq.get(s[r], 0) + 1
        if (r - l + 1) - max(freq.values()) > k:
            freq[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res
