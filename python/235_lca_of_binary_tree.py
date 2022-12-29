# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#  1) If the two values are both less than the root node, we can go left by setting the current node to current.left
#  2) If the two values are both greater than the rood node, we go right.
#  3) If one value is greater and the other less, we return the current node.

def lowestCommonAncestor(root, p, q):
    curr = root

    while curr:
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
        else:
            return curr
