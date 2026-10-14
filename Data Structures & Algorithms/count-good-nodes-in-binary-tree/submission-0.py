# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS + maximum passing from root down a path 
        # in cascading fashion (path-specific)
        # pre-order btw, but doesn't really matter for the incrementation

        count = 0

        def rec_dfs(node, largest):
            if node is None: return
            if node.val >= largest:
                nonlocal count
                count+=1
            if node.right is not None:
                rec_dfs(node.right, max(node.val, largest))
            if node.left is not None:
                rec_dfs(node.left, max(node.val, largest))
            return
            
        rec_dfs(root, float('-inf'))
        return count

        # time complexity : O(n)
        # space complexity : O(1)
        # btw : if the tree is too big to hold in our stack 
        # with this implementation we could either go 
        # for cps or an explicit stack to have it in the heap
        # memory of our process rather than the stack memory
        