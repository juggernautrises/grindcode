# https://leetcode.com/problems/container-with-most-water/
# Start with two pointers, one at the start and one at the end. Calculate the area by subtracting r-l to get the x
# value and multiplying by the min of value of height[l] vs height[r]. Compare it to the recorded max_area and update
# accordingly. Then check which pointer has the lowest height and increment or decrement and recalculate. Do this as
# long as l < r.

def maxArea(height):
    max_area = 0
    l = 0
    r = len(height) - 1
    while l < r:
        h = min(height[l], height[r])
        area = (r - l) * h
        max_area = max(area, max_area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area
