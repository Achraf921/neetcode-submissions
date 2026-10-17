"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # This actually sounds like a DFS with a set of visited nodes, to make sure we don't
        # indulge in any duplicates
        # rather than using a set of visited nodes, here we want to use a dictionary
        # to have a reference to any already-created clone ready to serve
        # when met again from another path/edge

        my_clones = {}

        def rec_dfs(node):
            if node is None: return None
            # we basically want to clone if not already existing, else we just return the 
            # reference to the already existing clone
            # and link to neighboors through recursing 
            # when do we actually create the nodes though ?
            # well what we could do is create if it doesn't already exist ofc
            if node in my_clones:
                return my_clones[node]
            else:
                clone = Node(node.val, [])
                my_clones[node] = clone
            for neigh in node.neighbors:
                if neigh in my_clones:
                    clone.neighbors.append(my_clones[neigh])
                else:
                    clone.neighbors.append(rec_dfs(neigh))
            # adding all neighs
            return clone
        
        return rec_dfs(node)




        