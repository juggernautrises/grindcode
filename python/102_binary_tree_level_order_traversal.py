# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Using a queue, we first add the root node to it. We then take the length of the queue and begin iterating through
# the length of it, popping off node each time and adding that value to the level list. We then add the children to the
# q and repeat the process while there is always a node in the queue.

import collections


def levelOrder(root):
    res = []
    q = collections.deque()
    q.append(root)
    while q:
        qlen = len(q)
        level = []
        for i in range(qlen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res
