class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # here, we need to do a BFS from the chests, and stop whenever we reach cells
        # who'se values are inferior to our distance from them (non-zero ofc)

        h, w = len(grid), len(grid[0])
        queue = deque()
        # we want to run multi-source bfs, s.t within a shared queue, chest one runs its 
        # neighboor-1 bfs, and chest 2 and on until they have all completed before moving to 
        # everyone's neighboor 2, which optimizes to O(h*w)
        for j in range(h):
            for i in range(w):
                if grid[j][i] == 0:
                    queue.append([j, i])

        while len(queue)>0: # we run ouf BFS
            # distance stuff
            my_node = queue.popleft()
            n, m = my_node
            # we want to walk every node that is walkable around us, assign it our
                        # distance if it doesn't already have something smaller going on
            # and add it to the queue if so, otherwise we don't add it
            for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
                if n+y>=0 and n+y<h and x+m>=0 and x+m<w and grid[y+n][x+m]==2147483647:
                    # this filters out for other chests, water and lower dist
                    # from another chest cells
                    # and we also filter for out of board ofc and mask
                    grid[n+y][m+x] = grid[n][m]+1
                    queue.append([y+n,x+m])
                    

        