# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse_base(node): # O(1)
            if node is None: return None
            saved_node = node.right
            node.right = node.left
            node.left = saved_node

        # now that we have the elementary revrsing func
        # let's run a post-order DFS with it

        def recursive_post_order_dfs(root):
            if root is None: return
            if root.left is None and root.right is None:
                # leaf base case
                reverse_base(root)
            else:
                recursive_post_order_dfs(root.left)
                recursive_post_order_dfs(root.right)
                reverse_base(root) # i.e post-order dfs

        # calling our function
        recursive_post_order_dfs(root)
        return root

        # time comp : O(n)
        # space comp : O(1)
