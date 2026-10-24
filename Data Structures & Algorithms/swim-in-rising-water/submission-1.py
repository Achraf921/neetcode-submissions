class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # here the initial backtracking approach is quite expensive (exp time)
        # but it seems that dijkstras approach to get the cheaper path is possible
        # if we see the grid as a directed positively weighted graph, let's implement it
        

        # this time I don't think we need an adjacncy list, let's just have our starts and our 
        # visited set, and our heap like we always do
        
        # we should also take into account that the earlier 'high' cells come, the more expensive
        # they are as we would have to stall there for a bit
        
        h, w = len(grid), len(grid[0])
        if h==1 and w==1: return grid[0][0]
        cost = {}
        # we initiallize all of our costs at 0
        # we also kinda need a time figure to be able to know at which time do we walk a cell
        # and hence if it requires any waiting time, we could include this into our heap objet
        heap = [[(grid[0][0]), [0,0]]] # cost, position
        visited = set()
        # we don't need the path in and of itself but just the cheapest path to final cell
        # and this is what dijkstras actually yields


        ## this problem is so fucking badly worded, makes you think swimming does take time
        # and we do need to sit idle to let the water rise, though here, you just 
        # wait for the water to raise in the optimal path, and micheal phelps your way to 
        # the end in O(0) 

        while len(heap)>0:
            # we always want to take the element with the smaller cost
            time, cell = heapq.heappop(heap)
            y, x = cell
            if (y, x) in visited: continue
            visited.add((y,x))
            for j, i in [[-1,0],[1,0],[0,1],[0,-1]]: # our 4 walking directions
                yk, xk = y+j, x+i
                if yk<0 or yk>h-1 or xk<0 or xk>w-1 or grid[yk][xk] in visited: continue
                neigh = grid[yk][xk]
                new_time = 0
                if neigh<=time:
                    new_time = time
                else:
                    new_time = neigh
                
                
                if ((yk, xk) in cost.keys() and cost[(yk,xk)]<=new_time) or (yk, xk) in visited:
                    continue # our edit is not optimal
                else:
                    cost[(yk,xk)]=new_time
                    heapq.heappush(heap, [new_time, (yk, xk)])
        
        return cost[(h-1,w-1)]
                
                



        

        