# https://leetcode.com/problems/maximum-product-subarray/submissions/

# Set the initial max prod to the max value of the array
# Since there are negative numbers, we need to calculate what the potential max value is and
# what the min value is for every number in the list. At each calculation of the current max prod,
# Check it against our answer

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
