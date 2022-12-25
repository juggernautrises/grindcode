# https://leetcode.com/problems/number-of-provinces/description/
# Set up a map of each node and what other nodes it connects to (ignoring itself).
# For each node, first check to see if it has already been visited. If it hasn't, perform a
# depth first search on it and increase the province count by one.
# DFS involves:
#   a) If the node has already been visited, return from the DFS
#   b)  Otherwise, add it to the visited list and for every child that it's connected to, perform DFS on it

def findCircleNum(isConnected):
    pmap = {i: [] for i in range(len(isConnected))}
    for i in range(len(isConnected)):
        for j in range(len(isConnected[i])):
            if isConnected[i][j] and i != j:
                pmap[i].append(j)
    provinces = 0
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for c in pmap[node]:
            dfs(c)

    for node in pmap:
        if node not in visited:
            dfs(node)
            provinces += 1

    return provinces


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
res = findCircleNum(isConnected)
print(res)
