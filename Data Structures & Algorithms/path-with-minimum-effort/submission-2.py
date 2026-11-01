class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # after trying the Backtraking approach, it TLEs, hence 
        # we need to use dijkstras here since max effort never
        # decreases (with a min heap and stuff)

        heap = []
        visited = set()
        # we will key on (x,y) and run dijkstras
        effort_map = {} #(y,x) -> dist
        effort_map[(0,0)]=0 # init
        heapq.heappush(heap, [0,0,0]) # [dist, y , x] # starting at 0,0
        h, w = len(heights), len(heights[0])
        while heap:
            e, y, x = heapq.heappop(heap) 
            if (y,x) in visited: continue
            visited.add((y,x)) # otherwise add it
            for j,i in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
                if i>=0 and i<w and j>=0 and j<h and (j,i) not in visited:
                    # we want to be restrictive/lazy
                    eff = abs(heights[j][i]-heights[y][x])
                    if (j,i) in effort_map and effort_map[(j,i)]<=max(e, eff): continue
                    # we skip adding it if it is on a better path
                    else:
                        effort_map[(j,i)]=max(e, eff)
                        heapq.heappush(heap,[max(e, eff),j,i])
        return effort_map[(h-1, w-1)]








