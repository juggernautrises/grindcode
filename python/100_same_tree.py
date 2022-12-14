# https://leetcode.com/problems/same-tree/

def isSameTree(p, q):
    if not p and not q:
        return True

    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right and q.right)
    return False
