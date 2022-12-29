# https://leetcode.com/problems/house-robber-ii/submissions/
# Same as house robber 1, but this time we call the function on a list which excludes the first item and a list which
# excludes the last item. We then get the max between those calls and the first element in the list since the list could
# be a single house

def rob(nums):
    def _rob(nums):
        first_house = 0
        second_house = 0
        for n in nums:
            og_second_house = second_house
            second_house = max(first_house + n, second_house)
            first_house = og_second_house
        return second_house

    return max(nums[0], _rob(nums[1:]), _rob(nums[:-1]))
