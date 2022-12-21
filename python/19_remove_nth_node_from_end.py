# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Add a dummy node to the start of the list and initialize a left pointer that points at this node. Create a right
# pointer that points to the head node. Move the right pointer n places and then begin moving both pointers by one until
# the list ends. Set the left.next to left.next.next.


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode()
    dummy.next = head
    l = dummy
    r = head
    for i in range(n):
        r = r.next
    while r:
        r = r.next
        l = l.next
    l.next = l.next.next
    return dummy.next
