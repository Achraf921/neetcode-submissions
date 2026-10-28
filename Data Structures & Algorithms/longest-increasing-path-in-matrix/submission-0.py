class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # this is almost a BFS graph traversal problem where the brute force 
        # would be to backtrack and try every single possible path
        # here though, it is kinda hard to find a base case as we don't really have a constraint
        # closed end, as we can sort of move up, down left and right from every cell
        # tbh what we could just do is to walk every cell
        # build the largest path through plain DFS, and only query the largest path
        # from cells that are larger than us, and since they are larger than us
        # we can NOT sit on their largest path as their largest path requires us to be strictly
        # larger, and I think doing this recursively, could result in no-overlap
        # this is hence a 2D DP problem where the state we keep is largest path from cell
        # (x, y), let's first try to implement this top-down with memoization

        memo = {}

        h, w = len(matrix), len(matrix[0])
        # if we see this matrix as an elevation map, peaks are our base cases
        # as they can't go anywhere but down, and will hence return one

        if h==1 and w==1: return 1 # single cell

        def memo_bfs(y, x):
            if (y, x) in memo: return memo[(y, x)]
        # mountain peaks are our base cases and will get picked out by the for loop's bool filter

            cur = matrix[y][x] # current value
            # we want to try all cells
            longest_path = 1 # only us
            for j, i in [[y+1,x], [y-1, x], [y, x+1], [y,x-1]]:
                if i<0 or i>w-1 or j<0 or j>h-1 or matrix[j][i]<=cur: continue
                # we don't want to walk/query void or a cell smaller or equal to us
                path = 1+memo_bfs(j, i)
                if path>longest_path:
                    longest_path = path
            
            memo[(y, x)] = longest_path
            return longest_path

        # we want to call the function on every cell, and since we keep the same memo
        # we never re-do any work

        best_path = 1
        for m in range(h):
            for n in range(w):
                best_path = max(best_path, memo_bfs(m, n))
        
        return best_path












        