class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def gen_neighbor(node):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for i, j in directions:
                if not(0 <= node[0] + i <= m - 1 and 0 <= node[1] + j <= n - 1):
                    continue
                if grid[node[0] + i][node[1] + j] == 0:
                    continue
                yield (node[0] + i, node[1] + j)
            
        def dfs(node):
            seen = set()
            queue = deque()
            queue.append(node)
            level = 0
            
            while queue:
                for _ in range(len(queue)):
                    cur_node = queue.popleft()
                    if cur_node in seen:
                        continue
                    seen.add(cur_node)
                    if grid[cur_node[0]][cur_node[1]] == 2:
                        #print("found", cur_node[0], cur_node[1])
                        return level
                    queue.extend(gen_neighbor(cur_node))
                    
                    #for neighbor in gen_neighbor(cur_node):
                    #    queue.append(neighbor)
                    
                level += 1
                #print("queue", queue)
            
            return -1
            
        m = len(grid)
        n = len(grid[0])
        time = 0
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_time = dfs((i, j))
                    #print(i, j, cur_time)
                    if cur_time == -1:
                        return -1
                    else:
                        if cur_time > time:
                            time = cur_time
        
        return time
