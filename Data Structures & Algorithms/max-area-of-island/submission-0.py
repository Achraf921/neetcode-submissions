class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS again here with a boolean mask to make sure we don't walk back on chunks we visited

        h, w = len(grid), len(grid[0])
        mask = [[True] * w for _ in range(h)]
        max_area = 0

        for j in range(h):
            for i in range(w):
                cur = grid[j][i]
                if cur == 1 and mask[j][i]:
                    local_area = 0
                    mask[j][i] = False # we don't want BFS to walk back here
                    queue = deque()
                    queue.append((j,i))
                    while len(queue)>0:
                        local_area += 1
                        y, x = queue.popleft()
                        # we want to expolore all 4 directions, to make sure we don't 
                        # get tricked by a U shaped island

                        if x+1<w and mask[y][x+1] and grid[y][x+1]==1:
                            mask[y][x+1]=False
                            queue.append((y, x+1))
                        
                        if x-1>=0 and mask[y][x-1] and grid[y][x-1]==1:
                            mask[y][x-1]=False
                            queue.append((y, x-1))

                        if y+1<h and mask[y+1][x] and grid[y+1][x]==1:
                            mask[y+1][x]=False
                            queue.append((y+1, x))
                        
                        if y-1>=0 and mask[y-1][x] and grid[y-1][x]==1:
                            mask[y-1][x]=False
                            queue.append((y-1, x))
                    if local_area > max_area:
                        max_area = local_area
        return max_area              



                    
        