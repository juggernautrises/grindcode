# https://leetcode.com/problems/minimum-window-substring/

import collections


def minWindow(s, t):
    """

    :param s: The full string
    :param t: The subtring
    :return:
    """
    # Create two dictionaries to keep track of the character counts.
    # Populate the count for the substring first
    t_count = collections.defaultdict(int)
    s_count = collections.defaultdict(int)
    for c in t:
        t_count[c] += 1
    res = (0, len(s))
    have = 0

    # The number of unique characters in the substring is how many
    # we need to match.
    need = len(t_count)
    l = 0
    # Iterate through the full string and create a sub window.
    for r, c in enumerate(s):
        # Begin keeping track of the character counts
        if c in t_count:
            s_count[c] += 1
            #  If the character counts match, we increased our matched count by 1.
            if s_count[c] == t_count[c]:
                have += 1
        # If the substring meets the requirements, we update the result length if it's smaller
        # We can then increment the left side (while removing the characters from the end) until
        # the string no longer matches the requirements.
        while have == need:
            if r - l < res[1] - res[0]:
                res = (l, r)
            if s[l] in t_count:
                s_count[s[l]] -= 1
                if s_count[s[l]] < t_count[s[l]]:
                    have -= 1
            l += 1
    return s[res[0]:res[1] + 1] if res[1] < len(s) else ''
