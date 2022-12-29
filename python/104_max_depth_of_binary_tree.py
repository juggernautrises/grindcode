# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# For the DFS solution, if the root node is none then the height of the node will be 0. Otherwise, the height is at
# least 1 plus the height of its child nodes. For this specific problem, we just want the max height of either child.

# DFS solution
def maxDepthRecursive(root):
    if not root:
        return 0

    return max(maxDepthRecursive(root.left), maxDepthRecursive(root.right)) + 1
