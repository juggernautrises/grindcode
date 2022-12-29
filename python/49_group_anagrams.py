# https://leetcode.com/problems/group-anagrams/
# One way to do this is simply sort the word  add it to the hashmap with the same sorted key.
# The other way (shown below) is to create an array from [0-25] for each word and then add the count of each letter in
# the word to the corresponding index. Convert this list to a tuple and use this as the key. Do the same for all the
# other words and add the entry to the hashmap.

import time


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    groups = {}
    for s in strs:
        count = [0 for _ in range(26)]

        for c in s:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        if key in groups:
            groups[key].append(s)
        else:
            groups[key] = [s]
    return groups.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = groupAnagrams(strs)
