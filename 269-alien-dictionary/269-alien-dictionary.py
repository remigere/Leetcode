class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # Kahn toplogical sorting
        
        if len(words) == 0:
            return ""
        
        if len(words) == 1:
            return "".join(set(words[0]))
        
        # create adj_list, hard part
        adj_list = defaultdict(set)
        indegree = defaultdict(int)
        
        """
        for i in range(len(words)):
            indegree[words[i][0]] = 0
            if len(words[i]) > 1:
                for j in range(len(words[i]) - 1):
                    adj_list[words[i][j]].add(words[i][j + 1])
                    indegree[words[i][j + 1]] = 0
        """
        for i in range(len(words) - 1):
            j = 0
            while j < len(words[i]):
                if j == len(words[i + 1]):
                    return ""
                if words[i][j] == words[i + 1][j]:
                    j += 1
                else:
                    adj_list[words[i][j]].add(words[i + 1][j])
                    break
        print(adj_list)
        
        
        
        # Kahn
        for i in range(len(words)):
            for j in range(len(words[i])):
                indegree[words[i][j]] = 0
        #print(indegree)
        # classic Kahn
        
        topo_order = []
        for src in adj_list:
            for dst in adj_list[src]:
                indegree[dst] += 1
        #print(indegree)
        queue = deque([k for k in indegree if indegree[k] == 0])
        
        while queue:
            vertex = queue.popleft()
            topo_order.append(vertex)
            for dst in adj_list[vertex]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    queue.append(dst)
        
        print(topo_order)
        
        return "".join(topo_order) if len(topo_order) == len(indegree) else ""
        """
        
        #dfs
        reversed_topo = []
        color = {}
        for i in range(len(words)):
            for j in range(len(words[i])):
                color[words[i][j]] = "WHITE"
        is_possible = True
        
        #print(color)
        #print(adj_list)
        def dfs(node):
            nonlocal is_possible
            color[node] = "GREY"
            #print(node)
            #print(node, adj_list[node])
            for dst in adj_list[node]:
                #print(dst, color[dst])
                if color[dst] == "WHITE":
                    dfs(dst)
                elif color[dst] == "GREY":
                    is_possible = False
                    #print(is_possible)
            color[node] = "BLACK"
            #print(node)
            reversed_topo.append(node)
            #print(reversed_topo)
        
        for node in color:
            #print("starting_node", node)
            if color[node] == "WHITE":
                dfs(node)
        #print(is_possible)
        return "".join(reversed(reversed_topo)) if is_possible else ""
        """