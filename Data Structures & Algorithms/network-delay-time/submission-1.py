class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # so I am guessing we are looking for the largest path in all of 
        # the shortest paths from the source node to all other nodes
        # this sounds a lot like a problem where getting all shortest 
        # paths from dijkstra's algorithm and then later picking the largest
        # value would work, let's try to implement it 

        # let's first build an adjacency list
        adj = {i:[] for i in range(1, n+1)}
        source_node = k
        # we want to add [time, node] pairs to the adj list
        for ui, vi, ti in times:
            adj[ui].append([ti, vi])
        
        # we also want to keep a set of visited nodes to not walk backwards
        visited = set()
        # we also need a mapping from the nodes to their distance time from
        # the source node to run dijkstras (we'll consider empty as +inf)
        dist = {}

        # btw we'll be using heapq, and for our tuples, heapq will priotirize
        # comparaison on the 1st element hence why we put time first
        heap = []
        heapq.heappush(heap, [0, source_node])
        while len(heap)>0:
            tcur, ncur = heapq.heappop(heap) # (time, node)
            if ncur in visited: continue # i.e if we visited it from another spot
            # checking all of its neighboors for a shorter possible path
            visited.add(ncur) # adding to visited set
            for t_neigh, n_neigh in adj[ncur]: # (time, node)
                if n_neigh in visited: continue # already visited
                if n_neigh in dist and dist[n_neigh]<=tcur + t_neigh: continue
                # finally
                dist[n_neigh] = tcur + t_neigh # distance + cost of walk
                heapq.heappush(heap, [tcur + t_neigh, n_neigh]) # only scenario where
                # we push
        # at the end, we should have updated all distances with minimal
        # distance, hence if the len of our dist is inferior to n, some 
        # nodes are missing
        print(len(visited))
        print(n)
        if len(visited)!=n: return -1
        else: return max(dist.values())



