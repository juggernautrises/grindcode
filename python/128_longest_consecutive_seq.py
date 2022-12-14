# https://leetcode.com/problems/longest-consecutive-sequence/description/
def longestConsecutive(nums):
    # We create a set (a lookup) of all the elements in the numbers array.
    # We then check to see if the number that comes before it (n-1) exists in the array
    # and, if it does not, we know that's the start of the sequence. We then increment to
    # the potential next number and if that number exists in the lookup / set, we can increase
    # the length. If the next number doesn't exist in the set then the sequence has ended and we
    # can check the max length
    lookups = set(nums)
    max_length = 0
    for n in nums:
        if n - 1 not in lookups:
            length = 1
            next_number = n + 1
            while next_number in lookups:
                length += 1
                next_number += 1
            max_length = max(max_length, length)
    return max_length


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
res = longestConsecutive(nums)
print(res)
