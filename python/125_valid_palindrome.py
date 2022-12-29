# https://leetcode.com/problems/valid-palindrome/
# 1) Create two pointers, one at the start (l0 and one at the end (r).
# 2) As long as the right pointers is greater than the left, increase the left pointer until it no longer points to an
#    alphanumeric character. Do the same with the right pointer
# 3) Check if the characters at r and l are different. Return false if they are, otherwise increment l and decrement r.

def isPalindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while r > l and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
