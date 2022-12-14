# https://leetcode.com/problems/clone-graph/description/
def cloneGraph(node):
    if not node:
        return node
    clones = {}

    def clone(node):
        if node in clones:
            return clones[node]
        clones[node] = Node(node.val)
        for neighbor in node.neighbors:
            clones[node].neighbors.append(clone(neighbor))
        return clones[node]

    return clone(node)
