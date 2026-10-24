class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # here this is almost a graph problem where we could run #
        # dijkstras, but since we have a DAG (tree) we
        # get to run DFS + memoization which is 
        
        # let's try this first and then see if we can converge to a 
        # tabulating solution to save on space

        memo = {}
        top = len(cost) # top
        # we want to record the minimum cost at the very base case
        # we actually need to do this in a non-tr way, hence we go down
        # then up and finally start returning to do top down
        def rec_dfs(k):
            if k in memo: return memo[k]
            if k>top-3: return 0
            # past top-3 is free

            one = cost[k+1]+rec_dfs(k+1)
            two = cost[k+2]+rec_dfs(k+2)
            best = min(one, two)
            memo[k]=best
            return best
        
        return rec_dfs(-1) # top-down memoization DFS
