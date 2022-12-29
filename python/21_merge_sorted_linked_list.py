# https://leetcode.com/problems/merge-two-sorted-lists/

# Create a dummy node for the new list. Set head to the dummy node.
# While the two lists are not null, check the value of the first against the second. Attach the smaller to the
# dummy.next node and advance the next item in the respective list. Advance the dummy node as well.
# After the loop completes, each list to see if there is anything left. Attach the remaining list to the next node
# of the dummy node. Return head.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    head = dummy
    while list1 and list2:
        if list1.val < list2.val:
            dummy.next = list1
            list1 = list1.next
        else:
            dummy.next = list2
            list2 = list2.next
        dummy = dummy.next

    if list1:
        dummy.next = list1

    if list2:
        dummy.next = list2

    return head.next
