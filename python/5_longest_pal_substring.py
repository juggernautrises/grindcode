# https://leetcode.com/problems/longest-palindromic-substring/description/

# For every index in the string, assume that it's the "middle" of a string. Expand outward by increasing the right
# pointer and decreasing the left as long as both characters at that index match. As long as both characters match,
# check the length of the string. If it's greater, update the max substring. Do the same process for potential
# substrings with an odd length.

def longestPalindrome(s):
    longest_pal = ''
    for i in range(len(s)):
        l = i
        r = i

        # Even substrings
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(longest_pal):
                longest_pal = s[l:r + 1]
            l -= 1
            r += 1

        l = i
        r = i + 1

        # Odd substrings
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(longest_pal):
                longest_pal = s[l:r + 1]
            l -= 1
            r += 1

    return longest_pal
