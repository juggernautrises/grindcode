# https://leetcode.com/problems/maximum-depth-of-binary-tree/


# DFS solution
def maxDepthRecursive(root):
    if not root:
        return 0

    return 1 + max(maxDepthRecursive(root.left), maxDepthRecursive(root.right))


# BFS Solution
def maxDepthIterative(root):
    stack = []
    level = 1
    stack.append((root, level))
    max_level = level
    while stack:
        node, level = stack.pop()
        if node.left:
            stack.append((node.left, level))

        if node.right:
            stack.append((node.right, level))
        level = level + 1
        max_level = max(level, max_level)
    return max_level
