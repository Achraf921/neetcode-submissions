# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # dfs where at each fork/parent, we compute
        # the sum of both paths + 1, compare it to max
        # and return the longest of the 2 paths + 1 to the parent
        # call
        max_len = float('-inf')
        def walker_dfs(node):
            if node is None: return 0
            left_len, right_len = 0, 0
            if node.left is not None:
                left_len = walker_dfs(node.left)
            if node.right is not None:
                right_len = walker_dfs(node.right)
            nonlocal max_len
            # since some paths may actually hurt us (as them
            # haing negative sums, we want to check
            # all possiblilites that include node.val)
            if right_len+left_len+node.val> max_len:
                max_len = right_len+left_len+node.val
            if right_len+node.val> max_len:
                max_len = right_len+node.val
            if node.val> max_len:
                max_len = node.val
            
            return (max(left_len, right_len, 0)+node.val)
        
        walker_dfs(root)
        return max_len
        
        # space complexity : O(1)
        # time complexity : O(n)
        