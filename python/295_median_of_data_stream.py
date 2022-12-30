# https://leetcode.com/problems/find-median-from-data-stream/
# Create two heaps: one for tracking the smaller values and one for tracking the larger values.
# Always add to the small heap and if the smaller heap grows larger by more than one, move it to the larger heap.
# When getting the median, if both lists are equal then return the average of the top two values. If one is bigger,
# pop off the value of the larger one and return it.
import heapq


class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            tmp = heapq.heappop(self.small)
            heapq.heappush(self.large, -tmp)

        if len(self.small) > len(self.large) + 1:
            tmp = heapq.heappop(self.small)
            heapq.heappush(self.large, -tmp)
        if len(self.large) > len(self.small) + 1:
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small, -tmp)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2
