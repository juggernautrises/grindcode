# https://leetcode.com/problems/subtree-of-another-tree/
# Uses the sameTree algo from a previous problem.
# First check if the two root nodes are the same tree. If they are, return True.
# Otherwise, check if the subRoot is a subTree of the left or right children of the root node.

def isSubtree(root, subRoot):
    if not subRoot:
        return True
    if not root:
        return False

    if sameTree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def sameTree(p, q):
    if not p and not q:
        return True

    if p and q and p.val == q.val:
        return sameTree(p.left, q.left) and sameTree(p.right, q.right)
    return False
