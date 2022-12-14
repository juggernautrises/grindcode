# https://leetcode.com/problems/invert-binary-tree/description/

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
