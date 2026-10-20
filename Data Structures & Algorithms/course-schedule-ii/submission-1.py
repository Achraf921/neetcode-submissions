class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # so here, this seems to be a topological sort algo again
        # where we don't just want to DFS and memoize but also keep
        # a walk order that worked
        # meaning, we may want to store all leaves, and then later walk 
        # the adjacency list starting from those leaves and it should solve
        # correctly
        # hence meaning we should keep one adj list for memoization, and one
        # for later walking that is still the accurate graph

        # let's first build our adj list

        adj = {course:set() for course in range(numCourses)}

        for course, pre in prerequisites:
            adj[course].add(pre)
        
        adj_mem = adj.copy()

        def rec_dfs(course, cache):
            if course in cache: return False # cycle
            if len(adj_mem[course]) == 0: 
                return True # leaf
            # we want to use the memoized version
            cache.add(course) # to make sure we don't cycle to it
            for c in adj_mem[course]:
                # we want to walk all of its pre-req
                noCycle = rec_dfs(c, cache)
                if not noCycle:
                    return False # i.e if a cycle was detected below
            # finally if we went throughh everything without every cycling
            # it means all of our pre-reqs did solve and we can hence clean
            # our list and remove ourselves from the cache/backtrack
            cache.remove(course)
            adj_mem[course]={}
            return True


        # now we want to DFS on all courses, memoization guarantees
        # we wont re-check a sub-graph/subtree
        valid = True # we'll keep track of cycles with it
        for course in range(numCourses):
            valid = valid and rec_dfs(course, set())
            if not valid:
                break # to break early in case of cycle

        # if valid is false, it means we did have a cycle in there
        if not valid:
            return [] # no path exists
        else:
            # we just need to walk from a leaf, to do so, we can check the adj
            # list (non-memoized) for one with no reqs
            leaves = []
            for k,v in adj.items():
                if len(v)==0:
                    leaves.append(k) # adding all of our leaves
            if len(leaves) is 0:
                raise RuntimeError('something is wrong')
            
            for leaf in leaves:
                adj.pop(leaf)

            # now we kinda want to bfs from all leaves using the 
            # un-memoized adj list graph now that we're sure that a path does
            # exist
            # and since we are guaranteed that this path exists, we can kind 
            # of have a re-try policy where if a req is missing
            # maybe another BFS is working to get to that req
            # and hence we add it at the end of the queue and retry
            # could  this ever deadlock though ? well just like in OSs
            # not unless there is a cycle, and since there are none, this
            # should be deadlock free

            path = leaves # we already have all leaves to start the path
            degree_audit = {leaf for leaf in leaves} # we already have all the
            while len(adj)>0:
                # we want to walk it till solved
                toremove = []
                for k,v in adj.items():
                    haveAllReqs = True
                    for pre in v:
                        if pre not in degree_audit:
                            haveAllReqs = False
                            break
                    # only if we have all pre-reqs we want to add to
                    # our path, degree audit and to remove
                    if haveAllReqs:
                        degree_audit.add(k)
                        path.append(k) # next taken
                        toremove.append(k) # we'll remove the pair from the adj
                
                # once we have iterated over all pairs, we remove all solved
                for key in toremove:
                    adj.pop(key) #removing all pairs and iterating if
                    # any remaining on our re-trial policy
        return path


                
                







        