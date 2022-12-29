# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# The Recursive Solution:
# Do an inorder DFS and add the node's value to a list. This list will be in sorted order and we can just return the
# kth / k-1 value from that list

def kthSmallestRecursive(root, k):
    res = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res[k - 1]


# The Iterative Solution
# Create a stack and track the current node. While the stack is not empty or there is a current node, we'll append the
# node to the stack and then go to the left value and repeat as long as there is a current / left node.
# We then pop a node off the stack and increase the n / tracker value by one. We test to see if we'd visited the
# required amount and, if not, we go to the right node and repeat the process\
def kthSmallest(root, k):
    stack = []
    cur = root
    n = 0
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        n += 1
        if n == k:
            return cur.val
        cur = cur.right
