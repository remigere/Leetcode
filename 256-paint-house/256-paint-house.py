class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        a, b, c = 0, 0, 0
        for i in range(len(costs)):
            new_a = min(b, c) + costs[i][0]
            new_b = min(a, c) + costs[i][1]
            new_c = min(a, b) + costs[i][2]
            a, b, c = new_a, new_b, new_c
        return min(a, b, c)
                