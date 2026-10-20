class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # this also kind of looks like a parallel BFS problem from the rotten fruits
        # where we keep the final max value if all fruits do end up rotten, otherwise
        # we return -1 so O(2*n*m)

        # let's first get all the rotten fruits
        queue = deque()
        h, w = len(grid), len(grid[0])

        for j in range(h):
            for i in range(w):
                if grid[j][i]==2:
                    queue.append([j,i])
        # now that we've got all fruits in the bin, let's run our bfs, and keep a tracker for the 
        # maximum value in there
        max_time = 2
        while len(queue)>0:
            n, m = queue.popleft()
            for y, x in [(-1,0),(1,0),(0,1),(0,-1)]:
                if x+m>=0 and x+m<w and y+n>=0 and y+n<h and grid[n+y][x+m]==1:
                    # we might need to slip in a quick -2 in (at the end idealy)
                    # as the rotten fruits start with 2
                    grid[n+y][x+m] = grid[n][m]+1 # it took a minute
                    if grid[n+y][x+m]>max_time:
                        max_time = grid[n+y][x+m]
                    queue.append([n+y, m+x])
        # once I have my max_time, I just want to check for any surviors to make my mind up 
        # about if I return max-2 or -1

        for j in range(h):
            for i in range(w):
                if grid[j][i]==1: return -1
        # if not :
        return max_time-2
        



        