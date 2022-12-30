# https://leetcode.com/problems/maximum-product-subarray/
# We have to calculate the min and max product at any given point.
# 1) Set the current min and current max to both one
# 2) Iterate through each number. If the number 0, reset the current min and current max to 1.
# 3) Set the current min and current max by multiply the current min and current max by the number, as well as the
# number by itself
# 4) Get the max product between the current min and current max on every iteration.
def maxProduct(nums):
    current_min = 1
    current_max = 1
    max_prod = max(nums)
    for i in range(len(nums)):
        n = nums[i]

        if n == 0:
            current_max = 1
            current_min = 1
            continue
        og_max = current_max
        current_max = max(current_min * n, current_max * n, n)
        current_min = min(current_min * n, og_max * n, n)

        max_prod = max(max_prod, current_max)
    return max_prod
