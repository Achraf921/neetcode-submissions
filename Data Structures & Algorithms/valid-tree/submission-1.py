class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # so the proporties of a tree are the following
        # no cyle, k-ary tree (i.e constant forking, k or less
        # distinct children per parent, and a single root that has no parent)
        # what I am thinking of is that we need to detect the root, as we'll
        # and build and adj list from all of the edges
        # moreover since those are un-directed edges, this adds complexity
        # as there is likely to be no clear root with no parent, since
        # the parent-child notion is directed

        # moreover, the notion of tree is actually looser than I described
        # since its undirected, we can sort of rotate the tree to make 
        # any node the root truly, and the k-ary concept disapears
        # the moment we set k to the node with largest adjaceny
        # the only standing constraint being cycles which 
        # pushes us towards topological sort cycle detection

        # let's first build our adj list

        adj = {i:[] for i in range(n)}
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        # but since we are adding to both, this adjency list may 
        # detect cycles though they are not, hence sparking the requirement
        # for a path set to be passed down the DFS
        # moreover since [0, 1] and [1, 0] pairs won't ever appear
        # we are guaranteed that no such cycle can exist, cycles 
        # have to go at least through another node before getting back
        # which means we should just pass that exact parent from which we came
        # from to be ignored


        def rec_dfs(node, cache, parent):
            if node in cache: return False #cycle
            if len(adj[node])==1 and adj[node][0]==parent or len(adj[node])==0:
                adj[node]=[]
                return True # leaf node
                # btw 0 is for the memoized-cleaned nodes

            # now we want to do DFS on the current node
            cache.add(node)
            for neigh in adj[node]:
                if neigh == parent: continue # we don't want to walk backwards
                else:
                    noCycle = rec_dfs(neigh, cache, node)
                    if not noCycle:
                        return False
            # finally if we walked all children paths without ever detecting
            # a cycle, we need to memoize, I feel like clearing the 
            # adj list of 0 is enough as it will render it as a leaf 
            adj[node]=[]
            cache.remove(node)
            return True # all solved
        
        # here this actually almost looks like plain DFS where memoization
        # doesn't really make sense, as a call from any node can traverse the 
        # whole graph since undirected ??
        # here memoizing actually allows us to check if everything got cleared
        # if some nodes still have connections, it means they have not been
        # walked and are hence not connected to us, so it does have a use

        hasNoCycle = rec_dfs(0, set(), None)

        for node in range(n):
            if len(adj[node])!=0:
                return False
        
        return hasNoCycle

        