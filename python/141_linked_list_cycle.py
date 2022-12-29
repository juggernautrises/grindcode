# https://leetcode.com/problems/linked-list-cycle/

# Iterate through each node in the list and check if it exists in the visited set. If it does, return True. Otherwise,
# add it to the visited set and continue to the next node.
def hasCycle(head):
    visited = set()
    cur = head
    while cur:
        if cur in visited:
            return True
        visited.add(cur)
        cur = cur.next
    return False
