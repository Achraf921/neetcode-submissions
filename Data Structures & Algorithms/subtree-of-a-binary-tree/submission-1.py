# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # this is a kind of similar exercise as the one to compare two 
        # binary trees, but here, we compare the subroot to every 
        # sub-tree of the root, probably through a parallel DFS here
        # but this comparaison must account for the extra branches
        # of the root's subtree
        
        # this would run in O(n*m) btw, m being the size of the
        # subtree
        def compare_dfs(root, subroot):
            if root is None and subroot is None: return True
            if root is None and subroot != None: return False
            if subroot is None and root != None: return False
            # both are non-null nodes
            left = compare_dfs(root.left, subroot.left)
            right = compare_dfs(root.right, subroot.right)
            state = (root.val == subroot.val) and left and right
            if state: return True 
        
        def compare_all_dfs(r):
            if r is None and subRoot is None: return True
            if r is None and subRoot != None: return False
            if subRoot is None and r != None: return False
            main = compare_dfs(r, subRoot)
            if main is True: return True
            left = compare_dfs(r.left, subRoot)
            if left is True: return True
            right = compare_dfs(r.right, subRoot)
            return compare_all_dfs(r.left) or compare_all_dfs(r.right)
        
        return compare_all_dfs(root)


        