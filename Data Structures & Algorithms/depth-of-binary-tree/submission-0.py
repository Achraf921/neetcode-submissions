# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # regular DFS, with maybe a max keeping from the root
        # not tr btw
        def rec_dfs(root, acc):
            if root is None: return acc
            else:
                left = rec_dfs(root.left, acc+1)
                right = rec_dfs(root.right, acc+1)
                return max(left, right)

        return rec_dfs(root, 0)