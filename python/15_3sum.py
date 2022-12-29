# https://leetcode.com/problems/3sum/

def threeSum(nums):
    # Sorting the numbers makes this easier.
    nums.sort()
    for i in range(len(nums)):
        a = nums[i]
        # If the index is not the first index, check if the one before it is the same value.
        # If it is, that means we can skip this loop because we already did the calculation
        if i > 0 and nums[i - 1] == a:
            continue

        # Create two pointers, one starting at the next number, the other starting at the end of the array.
        l = i + 1
        r = len(nums)
        # While the left is always less than the right...
        while l < r:
            # Get the values at l and r and add them with the current num
            b = nums[l]
            c = nums[r]
            s = a + b + c
            # If the sum is 0 we have a hit, so we can add it to the result array if it's not already in there.
            if s == 0:
                if [a, b, c] not in res:
                    res.append([a, b, c])
            # If the sum is too big, we decrement the right side by one
            elif s > 0:
                r -= 1
            # Too small, we increase l by one
            else:
                l += 1
        return res


n = [-1, 0, 1, 2, -1, -4]
res = threeSum(n)
print(res)
