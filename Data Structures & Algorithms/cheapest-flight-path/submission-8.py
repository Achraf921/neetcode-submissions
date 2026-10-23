class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # here the modified dijkstras approach is hell to implement 
        # and furthermore TLEs, we need to use Bellman-Ford
        # negative cycle detection algorithm
        # now, the reason why this actually

        # here the trick to link the cycle detection consequence to 
        # our actual goal, is to not relax all edges V-1 times
        # but only K+1 times as this is the max number of steps we can 
        # take, hence we either do reach the desired airport in that 
        # meantime through K+1 steps, on a maybe sub-optimal solution
        # price wise, or we never do and return -1
 
        cost = {i:float('+inf') for i in range(n)} #each airport
        cost[src] = 0 # start

        for _ in range(k+1):
            cost_updates = cost.copy()
            # to not do in place updates and hence accidentally walk
            # multiple steps in one iter if they are successive
            for s, d , price in flights: # our edges for our airports
                if cost[s] + price < cost_updates[d]:
                    # we compare to the newly found ones as a 
                    # path at step k may yeild a better price 
                    # then another path at step k too
                    cost_updates[d] = cost[s] + price
            cost = cost_updates
        # this will expand from src up to k+1 times
        # btw here what this does is bottom-up DP/tabulation 
        # from the source node, where we incrementally optimize
        if cost[dst] == float('+inf'): return -1
        return cost[dst] 
                

                
