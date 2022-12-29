# https://leetcode.com/problems/same-tree/
# If the two nodes are null, we can return True
# If they are both not null and their values match, we recursively call the same tree function on the respective
# left and right sides. Otherwise, we return False

def isSameTree(p, q):
    if not p and not q:
        return True

    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right and q.right)
    return False
