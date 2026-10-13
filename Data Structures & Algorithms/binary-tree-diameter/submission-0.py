# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_path = 0
        def no_acc_post_ord_dfs(node):
            if node is None: return -1 # -1 allows to count edges
            # instead of nodes
            if node.left is None and node.right is None: return 0
            left_edges = 1 + no_acc_post_ord_dfs(node.left)
            right_edges = 1 + no_acc_post_ord_dfs(node.right)
            my_max_path = left_edges + right_edges
            nonlocal longest_path
            if  my_max_path > longest_path:
                longest_path = my_max_path
            return max(left_edges, right_edges)
        no_acc_post_ord_dfs(root)
        return longest_path