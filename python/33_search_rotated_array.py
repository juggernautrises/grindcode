# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (r + l) // 2
        # If the middle is the target, return it
        if nums[mid] == target:
            return mid

        # If the left is less than or equal to the middle
        if nums[l] <= nums[mid]:
            # If the target is less than the left side or the target is more than the mid,
            # then the target exist on the right side of the array and we can move l to the mid.
            if target < nums[l] or target > nums[mid]:
                l = mid + 1
            # If the above isn't true, then target exists in this section and we can move r to mid.
            else:
                r = mid - 1
        # If left is greater than the mid
        else:
            # If the target is less than the mid or the target is greater than the right side
            # then the target exists in the other side of the array
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            # Otherwise, the target exists in this side of the array
            else:
                l = mid + 1
    return -1
