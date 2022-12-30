# https://leetcode.com/problems/non-overlapping-intervals/description/


def eraseOverlapIntervals(intervals):
    # Sort the intervals
    intervals.sort()
    # Store the last visited interval
    last_interval = intervals[0]
    remove = 0

    for interval in intervals[1:]:
        # If the start of the current interval is after the end of the previous one, we can update the last interval
        # to the current one.
        if interval[0] >= last_interval[1]:
            last_interval = interval
        # Otherwise, the current interval falls between the last one. We will update the last interval's end value
        # to whichever one ends earliest. We also increased the interval removal value by one.
        else:
            remove += 1
            last_interval = [last_interval[0], min(last_interval[1], interval[1])]
    return remove
