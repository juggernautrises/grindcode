# https://leetcode.com/problems/validate-binary-search-tree/
# Valid Binary search tree requirements: Everything on the left should be less than the root and everything on the right
# should be greater.
# Recursively, we test the current node's status by comparing it against a left bound and a right bound. We then test it
# on the children by updating the left and right bounds to the current node's value

def isValidBST(root):
    def valid(node, left_bound, right_bound):
        if not node:
            return True

        if not (left_bound < node.val < right_bound):
            return False
        print(left_bound, right_bound)
        return valid(node.left, left_bound, node.val) and valid(node.right, node.val, right_bound)

    return valid(root, float('-inf'), float('inf'))
