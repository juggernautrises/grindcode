# https://leetcode.com/problems/reorder-list/
#   1) Find the middle node. Create a second list where the middle node is head
#   2) Reverse the second list
#   3) Iterate through the second list. Hold copies of the upcoming nodes for each list. Set the next value of the first
#      list's node to the second list's node. Set the second list's next node to the copied first and set the first
#      list's head node to the same copied value. Set the second list's head node to the copied second value.
def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    slow = head
    fast = head.next
    # Get the middle node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    first = head

    # Create a second list where the middle node is the start
    second = slow.next
    slow.next = None
    prev = None

    # Reverse the second list
    while second:
        tmp_next = second.next
        second.next = prev
        prev = second
        second = tmp_next
    second = prev

    # Merge the two lists
    while second:
        tmp_first = first.next
        tmp_second = second.next
        first.next = second
        second.next = tmp_first

        first = tmp_first
        second = tmp_second
