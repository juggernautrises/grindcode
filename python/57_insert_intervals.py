# https://leetcode.com/problems/insert-interval/

# Iterate through the entire list of intervals. For each interval, the following conditions could occur:
#   1) The interval ends before the newInterval begins, in which case we add the current interval
#   2) The interval starts after the newInterval ends therefore we can add the newInterval. This also means that all
#      remaining intervals also come after the new intervals, so we can return our current result list along with the
#      remaining intervals in the original list
#   3) If neither of the above conditions are true, that means we need to merge the interval by taking the min of
#   the start and the max of the end values to create an updated interval.
# If the new interval never comes before another interval, we need to add it at the end of the loop to the end of the
# new result array.

def insert(intervals, newInterval):
    res = []
    for i in range(len(intervals)):
        interval = intervals[i]
        if interval[1] < newInterval[0]:
            res.append(interval)
        elif interval[0] > newInterval[1]:
            res.append(newInterval)
            return res + intervals[i:]
        else:
            newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
    res.append(newInterval)
    return res
