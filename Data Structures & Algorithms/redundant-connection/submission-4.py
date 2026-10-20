class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # here we can use a DSU datatructure for path detection
        # the trivial version is quick-find
        # but the optimal is the quick-union version. with path-compression
        # and rank by height

        # here we first need to assume that everything is disjoint and then 
        # later join when we have proof of connectivity

        dss = {i:i for i in range(1, len(edges)+1)}

        def find_leader(node):
            cur = node
            while dss[cur]!=cur:
                prev = cur
                cur = dss[cur]
                dss[prev] = dss[cur] # path compression as we walk
            return cur

        for e1, e2 in edges:
            # if two nodes have the same leader, they are among the same set
            # and hence introduce a cycle
            l1, l2 = find_leader(e1), find_leader(e2)
            if l1 == l2:
                return [e1, e2]
            else:
                # we join them as they were two truly-join disjoint sets
                dss[l1]=l2 # joining the sets is joinging the leaders
        

        

        