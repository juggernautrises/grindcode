# https://leetcode.com/problems/product-of-array-except-self/

# Create a result array as big as nums where each value is defaulted to 1.
# Initialize a prefix variable to one
# Loop through the array from start to end and set the result array at the current index to the value of the prefix
# variable.
# Multiply the prefix by the current value of nums
# Create a suffix variable and initialize it to 0 and loop through the array going backwards
# Multiply the result array at the current index by the suffix
# Calculate the new suffix my multiplying it by the value of nums at the current index.

def productExceptSelf(nums):
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    # Prefix can be reused and reinitialized to 1 here. Left it in for clarity./
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result
