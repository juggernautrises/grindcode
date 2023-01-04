# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Create two pointers, one at the start and one at the end. Calculate the target. If the target is
# too small, increment the left pointer. If it's too big, decrement the right pointer.

def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]

        if s > target:
            r -= 1
        if s < target:
            l += 1
