# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Create pointers at the start and end of array. While the left pointer is less than or equal to the right
# pointer, check if left < right. If so, the array is sorted and we can take the first value as the min.
# Otherwise, we check if the mid value is greater than the right and, if so, we move the left to the mid
# point and repeat the process. Otherwise, we move the right to the mid and repeat.

def findMin(nums):
    l = 0
    r = len(nums) - 1
    min_val = nums[0]
    while l <= r:
        if nums[l] < nums[r]:
            return min(min_val, nums[l])

        mid = (l + r) // 2
        min_val = min(min_val, nums[mid])
        if nums[mid] >= nums[r]:
            l = mid + 1
        else:
            r = mid - 1
    return min_val
