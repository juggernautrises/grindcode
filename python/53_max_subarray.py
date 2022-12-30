# https://leetcode.com/problems/maximum-subarray/
# Kadane's algorithm:
# Set up a DP array. Set the first entry to the first value of nums. For every number starting at the
# first index / second value, check if the current index + the previous value is greater than just the current
# number by itself. Update the array and return the max value of the DP array.

def maxSubArray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

    return max(dp)
