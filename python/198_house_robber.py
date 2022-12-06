def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # [first_house, second_house, n]
    # At any point, we want the max value of n + first_house or just second_house alone
    # We take that max value, set it the value what will not be the second house (when we increment)
    # and set the value of the first house equal to what was once the second house

    first_house = 0
    second_house = 0
    max_value = 0
    for n in nums:
        max_value = max(n + first_house, second_house)
        old_second_house = second_house
        second_house = max_value
        first_house = old_second_house
    return max_value


houses = [1, 2, 3, 1]
res = rob(houses)
print(res)
