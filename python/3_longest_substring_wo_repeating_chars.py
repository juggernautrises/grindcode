# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Start with two pointers (l and r), both starting at index 0. r will always be increased.
# If r exists in the set already, we remove the l value and increase l, all while the r value continues
# to exist in the array. One the r value ceases to exist in the set. We continue with our loop.
# We then add the r value to the set and calculate the length (r-l +1) and update the max length.

def lengthOfLongestSubstring(s):
    l = 0
    res = 0
    char_set = set()

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        res = max(res, r - l + 1)
    return res
