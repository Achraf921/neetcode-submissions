# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # when walking the bst, we can either fork to the > side (right)
        # or the < side (left), and so the first fork happens at root
        # if it does fork, then the common ancestor is root, else we 
        # keep walking the shared path until it actually forks and 
        # return as soon as it does, as the forking element is the
        # common ancestor
        cur = root
        while True:
            num = cur.val
            if p.val < num and q.val <num: # left side of the shared branch
                cur =cur.left # we NEED strict equality btw
            elif p.val> num and q.val> num:
                cur = cur.right
            else:
                #we do have a fork
                return cur








        
        