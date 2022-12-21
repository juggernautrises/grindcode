# https://leetcode.com/problems/merge-k-sorted-lists/submissions/

# Iterate through each list and add the head value to the min heap, along with the index of the list that it's coming
# from. Pop from the min heap and add it to as a new node to a new linked list. Find the original list using the
# associated index and move to the next node. Add that new value to the min heap
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    dummy = ListNode()
    head = dummy
    heap = []
    for index, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, index))

    while heap:
        val, index = heapq.heappop(heap)
        head.next = ListNode(val=val)
        if lists[index].next:
            lists[index] = lists[index].next
            heapq.heappush(heap, (lists[index].val, index))
        head = head.next
    return dummy.next
