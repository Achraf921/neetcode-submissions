class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # this is a minimum spanning tree problem (MST)

        # by definition of a tree, we will use n-1 edges that NEED
        # to span the whole set of vertices

        # we also want to minimize the cost of the sum of all edges
        
        # We need to run Prim's Algorithm:
        # start from any node, assume you have adjacency to all 
        # nodes in the graph, we also need a visited set to make 
        # sure we actually output a tree, and a frontier min-heap
        # to greedyly pick the cheapest option from every node 
        # (kinda similar to dijkstras)
        # and we stop execution when the visited set's length
        # reaches n
        # and we keep track of the cost of all edges that we 
        # are actually taking on

        def mhtn(a,b):
            x1, y1 = a
            x2, y2 = b
            return abs(x1 - x2) + abs(y1-y2)
        
        # let's build our adjacency list (all to all) well we don't 
        # need one I guess since its all to all unless visited

        count = 0 # we will increment as we visit

        heap = [[0, points[0]]]
        n = len(points)
        visited = set()
        
        # building up our MST
        while len(visited)!=n and len(heap)>0:
            dist, point = heapq.heappop(heap)
            x, y = point
            if (x, y) in visited: continue # already visited
            count+= dist # building up our cost
            visited.add((x,y))

            for xk, yk in points:
                if (xk, yk) in visited: continue
                # otherwise we just compute the distance from current node
                # and push
                d = mhtn([xk,yk], [x,y])
                heapq.heappush(heap, [d, [xk, yk]])
        
        return count



