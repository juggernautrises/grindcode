# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Recursively create the left and half subtrees by finding the index of the root value in the inorder array
# and supplying all the values before the index to the left and all the values after to the right subtree call

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = TreeNode(val=preorder[0])
    pos = inorder.index(root.val)
    root.left = buildTree(preorder[1:pos + 1], inorder[:pos])
    root.right = buildTree(preorder[pos + 1:], inorder[pos + 1:])
    return root
