# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # post-order DFS again, passing up the 'delta' this time
        def pdfs(node):
            if node is None: return -1
            if (node.left is None and node.right is None): return 0
            left = 1 + pdfs(node.left)
            right = 1 + pdfs(node.right)
            delta = abs(left-right) # we'll use for poisioning
            # starting
            if left==-66 or right == -66 or delta>1:
                # -66 since we add one
                # this starts the poison checking delta, and then 
                # propagatest to every parent of a poisoned tree
                return -67
            else:
                return max(left, right) # othrwise, we return the longest
                # branch of our balanced tree
        delta = pdfs(root)
        return False if delta==-67 else True
        