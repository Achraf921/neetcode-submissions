# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # this actually looks like a regular DFS where we need to 
        # ofc start on the right, and keep track of what is the 
        # all-time max that has been reached to not write on
        # left-er paths that do not surpass what the 1st/couple
        # first walks achieved in terms of depth
        # pre-order dfs btw

        sol = []
        depth_record = 0

        def rec_dfs(root, depth):
            if root is None: return
            nonlocal depth_record, sol
            if depth>depth_record: # don't write on non-exposed nodes
                depth_record = depth
                sol.append(root.val)
            if root.right is not None:
                rec_dfs(root.right, depth+1)
            if root.left is not None:
                rec_dfs(root.left, depth+1)
            return
        
        rec_dfs(root, 1)
        return sol

        # time : O(n)
        # space : worst case O(n), on a regular-ish, balanced-ish
        #binary tree, O(logn)
        

            