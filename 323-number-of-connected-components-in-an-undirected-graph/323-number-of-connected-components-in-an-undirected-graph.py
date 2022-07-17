"""
class Union:
    def __init__(self, n):
        self.n = n
        self.rank = [0] * n
        self.root = [i for i in range(n)]
    
    def find(self, x):
        while self.root[x] != x:
            x = self.root[x]
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.n -= 1
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    
    def count(self):
        return self.n


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #union-find
        uf = Union(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.count()
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ele = set([i for i in range(n)])
        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        visited = set()
        queue = deque()
        count = 0
        while len(visited) < n:
            queue.append(next(iter(ele - visited)))
            count += 1
            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                queue.extend(adj[node])
        return count
            