# https://leetcode.com/problems/two-sum/

# For every number, first check if it exists in the hashmap and return the current num's index along with the
# corresponding index from the hashmap. Using the target-number as a key, add the current index as the value so
# it can be looked up later.

def twoSum(nums, target):
    tracker = {}
    for i in range(len(nums)):
        if nums[i] in tracker:
            return [i, tracker[nums[i]]]
        tracker[target - nums[i]] = i
