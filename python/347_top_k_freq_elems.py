# https://leetcode.com/problems/top-k-frequent-elements/
# 1) Create a hashmap that tracks the item count
# 2) Create an array that as indexes from 0-nums (the potential lowest count to the potential highest count of a
#    item in nums
# 3) Iterate through the hashmap and add the item to the index / count associated with it.
# 4) Iterate backwards through the array and add items until k elements have been added to the result array

def topKFrequent(nums, k):
    tracker = {}
    counter = [[] for _ in range(0, len(nums) + 1)]
    for num in nums:
        tracker[num] = tracker.get(num, 0) + 1
    for num, count in tracker.items():
        counter[count].append(num)
    res = []

    for i in range(len(counter) - 1, 0, -1):
        for j in counter[i]:
            res.append(j)
            if len(res) == k:
                return res
