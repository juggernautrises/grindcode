# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        res = []

        # Do a preorder traversal on the tree
        def preorder(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return '#'.join(res)

    def deserialize(self, data):
        vals = data.split('#')
        self.i = 0

        # Perform a reverse DFS
        # Take the value at the current index
        # Increment the index
        # Set the left tree by recursively calling DFS
        # Set the right tree by recursively calling DFS

        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(val=int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
