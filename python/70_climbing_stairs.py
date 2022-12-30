# https://leetcode.com/problems/climbing-stairs/

# There is one way to perform one step and one way to perform two steps. Three steps would be the number of ways for
# one step and two steps combine.

def climbStairs(n):
    one_step = 1
    two_step = 1
    for n in range(n - 1):
        old_two_step = two_step
        two_step = one_step + two_step
        one_step = old_two_step
    return two_step
