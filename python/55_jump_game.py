# https://leetcode.com/problems/jump-game/
# The last index is our "goal" so we iterate backwards, starting at the second to last element. We take the value
# at the current index and it to the index. If it makes it to the target index, we update the target_index to the
# current index and move on to the next value in the array. If the target index ends up at 0 (the start) at the end of
# the loop, we can return true since that means we can make it all the way to the end of the goal.

def canJump(nums):
    target_index = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums >= target_index:
            target_index = i
    return target_index == 0
