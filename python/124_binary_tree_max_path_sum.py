# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# For each node, calculate the max path to the left side and the max path to the right side.
# The maximum path would be the current node value + the left max value + the right max value.
# Since we can only go down one direction, we find which side is greater and return that combined
# with the node's current value.
def maxPathSum(root):
    res = [root.val]

    def max_path(node):
        if not node:
            return 0
        left_max = max_path(node.left)
        right_max = max_path(node.right)

        left_max = max(0, left_max)
        right_max = max(0, right_max)
        res[0] = max(res[0], node.val + left_max + right_max)
        return node.val + max(left_max, right_max)

    max_path(root)
    return res[0]
