class Solution:
    white = 0
    grey = 1
    black = 2
    
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        cycle = False
        
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
        color = {i: Solution.white for i in range(n)}
        is_possible = True
        
        def dfs(node):
            nonlocal is_possible
            
            #early return
            color[node] = Solution.grey
            if node not in adj_list:
                if node != destination:
                    print("here")
                    is_possible = False
                    return
            for nei in adj_list[node]:
                if color[nei] == Solution.white:
                    dfs(nei)
                #cycle
                elif color[nei] == Solution.grey:
                    is_possible = False
                    return
            color[node] = Solution.black
        
        dfs(source)
        
        return is_possible