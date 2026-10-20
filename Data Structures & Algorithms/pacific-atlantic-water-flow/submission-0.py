class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # Here this is again an example of reverse thinking, we will here 
        # want to find out from the atlantic ocean, which cells can reach it (climbing instead
        # of falling using a concurent BFS) and do the same mechanism for the pacific
        # and keep a tuple mask of the array, and collect all (True, True) elements 
        # at the end

        # let's get all of our pacific touching nodes
        h, w = len(heights), len(heights[0])
        pacific = deque([[i,0] for i in range(h)] + [[0, j] for j in range(w)])
        # gettign all of our atlantic ones too
        atlantic = deque([[i,w-1] for i in range(h)] + [[h-1, j] for j in range(w)])

        tup_mask = [[[False, False] for _ in range(w)] for _ in range(h)] # left True if for pacific, right is
        # for pacific
        for y, x in pacific:
            tup_mask[y][x][0]=True
        #for atlantic:
        for y, x in atlantic:
            tup_mask[y][x][1]=True

        # now we first want to run parallel bfs
        # on both
        cur_queue = pacific
        isAtlantic = False
        while len(cur_queue)>0:
            # we are allowed to climb, which is the logical inverse of dropping, i.e only
            # higher or equal cells to our current elevation
            y, x = cur_queue.popleft()
            for j, i in [[-1,0],[1,0],[0,-1],[0,1]]:
                yk, xk = y+j, i+x
                if yk>=0 and yk<h and xk>=0 and xk<w and heights[yk][xk]>=heights[y][x]:
                    # we need a way to check if we're working on pacific or atlantic rn
                    if isAtlantic and not tup_mask[yk][xk][1]: #atlantic walk scenario
                        tup_mask[yk][xk][1]=True
                        cur_queue.append([yk,xk])
                    if not isAtlantic and not tup_mask[yk][xk][0]: #pacific walk scenario
                        tup_mask[yk][xk][0]=True
                        cur_queue.append([yk,xk])
            # we'll use this guard to flip to the atlantic bfs using the same loop
            if not isAtlantic and len(cur_queue)==0:
                isAtlantic=True
                cur_queue = atlantic # swithcing it up

            # finally, collect what our concurrent BFSs have yielded in the mask
        sol = []
        for y in range(h):
            for x in range(w):
                if tup_mask[y][x][0] and tup_mask[y][x][1]:
                    sol.append([y,x])

        return sol



        
        