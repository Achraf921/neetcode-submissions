class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # this seems to be a scan of the grid + BFS when we hit land with 
        # a boolean mask to not re-count islands

        h, w = len(grid), len(grid[0])
        mask = [[True] * w for _ in range(h)] # all trues at initializaiton
        island_counter = 0

        for i in range(h):
            for j in range(w):
                cur = grid[i][j]
                if cur == '1' and mask[i][j]:
                    island_counter+=1
                    mask[i][j] = False # setting cur cell to False, no one will do it for us in BFS
                    queue = deque() # for bfs
                    queue.append((i,j))
                    while len(queue)>0:
                        # we have UP to 4 neighboors
                        # we DO NEED ALL 4 paths, as a weird, U-shaped island could 
                        # trick us if we only walked down and right, though the 
                        # for loop's walking order is left->right up-> down
                        y, x = queue.popleft()
                        # up neighboor
                        if x+1<w and mask[y][x+1] and grid[y][x+1]=='1':
                            # we just want to flip it to false for it not to be 
                            # masked again, and add it to the queue to explore with bfs
                            mask[y][x+1] = False
                            queue.append((y,x+1))
                        if x-1>=0 and mask[y][x-1] and grid[y][x-1]=='1':
                            # we just want to flip it to false for it not to be 
                            # masked again, and add it to the queue to explore with bfs
                            mask[y][x-1] = False
                            queue.append((y,x-1))
                        if y+1<h and mask[y+1][x] and grid[y+1][x]=='1':
                            # we just want to flip it to false for it not to be 
                            # masked again, and add it to the queue to explore with bfs
                            mask[y+1][x] = False
                            queue.append((y+1,x))
                        if y-1>=0 and mask[y-1][x] and grid[y-1][x]=='1':
                            # we just want to flip it to false for it not to be 
                            # masked again, and add it to the queue to explore with bfs
                            mask[y-1][x] = False
                            queue.append((y-1,x))
                else:
                    continue

        return island_counter






        