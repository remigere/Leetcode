from sortedcontainers import SortedList
class UnionFind:
    def __init__(self, size: int) -> None:
        self.group = [0] * size
        self.rank = [0] * size
        
        for i in range(size):
            self.group[i] = i
      
    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        # node1 and node2 already belong to same group.
        if group1 == group2:
            return False

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

        return True
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        if len(points) <= 1:
            return 0
        
        def dist(pi, pj):
            return abs(pi[0] - pj[0]) + abs(pi[1] - pj[1])
        
        S = SortedList()
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                S.add((dist(points[i], points[j]), i, j))
        visited = set()
        k = -1
        res = 0
        used = 0
        
        uf = UnionFind(n)
        while used < n - 1:
            k += 1
            s, i, j = S[k]
            if uf.join(i, j):
                used += 1
                res += s
            
        return res
            