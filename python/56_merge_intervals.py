# https://leetcode.com/problems/merge-intervals/description/

# Sort all the intervals by start value and initialize the return array with the first value from the sorted interval
# array. Starting with the second interval, loop through each interval and grab the last value from the result array.
# Compare the new interval with the last added one:
#   1) If the start value of the current interval comes after the last interval in the result array, add the current
#      interval.
#   2) Otherwise, merge the current interval with the last added value and update the last element in the result array.
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        current = intervals[i]
        merged_interval = res[-1]
        if current[0] > merged_interval[1]:
            res.append(current)
        else:
            res[-1] = [min(merged_interval[0], current[0]), max(merged_interval[1], current[1])]
    return res
