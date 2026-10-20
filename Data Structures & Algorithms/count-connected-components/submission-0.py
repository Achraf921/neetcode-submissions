class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # here we could just build the adj list and then DFS/BFS 
        # arbitrarly a node and remove it from the adj list recurcively
        # until done, and if the adj list still contains nodes
        # then there is at least one other component

        adj = {i:[] for i in range(n)}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1) # undirected
        
        # now let's build our dfs algorithm to be destructive

        def rec_dfs(node, visited):
            if node in visited: 
                # either a cyle or the end of a path
                return
            # but we don't want to indulge in it to not infinite loop
            visited.add(node)
            for neigh in adj[node]:
                rec_dfs(neigh, visited)
            # whenever poped all my paths, I'll pop my self too
            adj.pop(node)

        # this actually seems to work
        # we always have at least 1 node meaning we don't need to edge case if
        component_counter = 1 # we always have at least one
        while len(adj)>0:
            # arbitrary key
            rec_dfs(next(iter(adj.keys())), set()) # arbitrary
            # if after that we still have items we increment
            if len(adj)>0: # i.e we have a surviving component
                component_counter+=1
        
        return component_counter

        # this runs in O(n) time and space 
            

        