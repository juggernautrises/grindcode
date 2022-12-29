# https://leetcode.com/problems/reverse-linked-list/description/
# 1) Initialize current by setting it to the head and previous to None.
# 2) As long as the current node is not None...
# 3) Hold the next node as a temp value since we'll be breaking the link to it
# 4) Point the current's next node to the previous value
# 5) Set previous to the current value
# 6) Set the current value to the temporary next node.

def reverseList(head):
    previous = None
    current = head
    while current:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
    return previous
