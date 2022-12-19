# https://leetcode.com/problems/longest-increasing-subsequence/

# Set each initial LIS array to one since the longest subseq at any given point would be one.
# For each index, check the previous indices before it. If any of those indices are less,
# add one to the value and take the max of that value vs. what already exists as a value for the
# index we're currently looking at.
def lengthOfLIS(nums):
    LIS = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                LIS[i] = max(LIS[i], LIS[j] + 1)
    return max(LIS)
