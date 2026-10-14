# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # ok so what I was thinking of is a poisoning
        # post-order dfs where we go all the way down the leaf's
        # parents, check the condition
        # return a boolean, and also check the condition for the grandpas
        # on both the children's condion (poisoning)
        # and the values

        # [9, 3, 12, 1, 10, None, None], this breaks from having a 
        # [9, 3, 12, 2, 5, None, None, None, 4, None , None]
        # bigger value in the left sub tree than the root, we 
        # should account for such cases in both bigger and smaller scnearios

        # we actually do need to run the local checks as well as the down-passed
        # maximums and minimums I guess, to run a global consistecy check at every
        # level

        # we should actually return both max and min
        def dfs_bst(node) -> (int, int, bool): 
            # here, we explictely state all scenarios but the else
            if node.left is not None and node.right is not None:

                max_left, min_left, booleft = dfs_bst(node.left)
                max_right, min_right, boolright = dfs_bst(node.right)

                our_bool = max_right > node.val and min_right>node.val and min_left<node.val and max_left<node.val and booleft and boolright

                # our conditions are pretty long
                return max_right, min_left, our_bool




            elif node.left is not None and node.right is None:
                max_left, min_left, booleft = dfs_bst(node.left)

                our_bool = min_left<node.val and max_left<node.val and booleft

                return node.val, min_left, our_bool
            
            elif node.right is not None and node.left is None:
                max_right, min_right, boolright = dfs_bst(node.right)

                our_bool = min_right>node.val and max_right>node.val and boolright

                return max_right, node.val, our_bool
            else: # when both children are none
                return node.val, node.val, True



        _ , _ , final_bool = dfs_bst(root)
        return final_bool

        #O(n) time, O(n) space, 

        ## !! btw when reading a tree array, null's don't get children !!!


        