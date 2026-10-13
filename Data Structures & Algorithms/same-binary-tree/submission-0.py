# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # maybe this is some kind of parallel DFS where at each step 
        # we compare
        def parallel_p_dfs(node1, node2):
            if node1 is None and node2 is None: return True
            if node1 is None and node2 != None: return False
            if node2 is None and node1 != None : return False
            else:
                left = parallel_p_dfs(node1.left, node2.left)
                right = parallel_p_dfs(node1.right, node2.right)
                return (node1.val == node2.val and left and right)
        return parallel_p_dfs(p,q)
        