# https://leetcode.com/problems/merge-k-sorted-lists/
# For every list, take the first value of the node and add it to a min heap, along with the index to the source list.
# While there are still items in the min heap, add it as the next node to the new list. Once you pull a value off the
# heap, we'll need to replace that value with the next value from the list associated to with it.
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
