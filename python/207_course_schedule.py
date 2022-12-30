# https://leetcode.com/problems/course-schedule/
# Basically, try and detect a cycle. Set up a graph / map of the courses and prereqs. Do a DFS on each course and mark
# the course as visited. Perform a dfs on each child and check if any of the course have been visited. If there is
# no cycle, we can set the course prereqs to 0 / empty list to we can traverse it faster and not duplicate work.

def canFinish(numCourses, prerequisites):
    pmap = {}
    visited = set()
    for crs, pre in prerequisites:
        if crs not in pmap:
            pmap[crs] = [pre]
        else:
            pmap[crs].append(pre)

    def dfs(crs):
        if crs not in pmap or not pmap[crs]:
            return True
        if crs in visited:
            return False
        visited.add(crs)
        for p in pmap[crs]:
            if not dfs(p):
                return False
        visited.remove(crs)
        pmap[crs] = []
        return True

    for crs in pmap:
        if not dfs(crs):
            return False
    return True
