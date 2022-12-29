# https://leetcode.com/problems/invert-binary-tree/description/
# Start at the root. Switch the left and right nodes for the provided root node. Recursively call the invert function
# For the new left and new right node.
def invertTree(root):
    def invert(node):
        if not node:
            return
        tmp = node.left
        node.left = node.right
        node.right = tmp
        invert(node.left)
        invert(node.right)

    invert(root)
    return root
