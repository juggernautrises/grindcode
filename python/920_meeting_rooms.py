# https://www.lintcode.com/problem/920/
# Take the intervals in pairs and check if the start time for the second interval is less than the
# end time before the first.
def can_attend_meetings(intervals):
    intervals.sort()

    for i in range(1, len(intervals)):
        interval1 = intervals[i-1]
        interval2 = intervals[i]
        if interval2[0] < interval1[1]:
            return False
    return True


intervals = [(0, 30), (5, 10), (15, 20)]
res = can_attend_meetings(intervals)
intervals = [(5,8),(9,15)]
res = can_attend_meetings(intervals)

print(res)
