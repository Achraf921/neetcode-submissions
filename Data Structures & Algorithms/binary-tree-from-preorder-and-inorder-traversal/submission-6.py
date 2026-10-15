# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we need to fucking hash ts
        # while keeping our slicing abilities
        # I guess we just hash inorder up, and rather than calling .index()
        # on it, we'll call onto the dict

        hashed_inorder = {k:v for k,v in zip(inorder, range(len(inorder)))}
        
        def buildTreeWithHash(idx, lo, hi):
            if lo>hi: return None # base case
            root = TreeNode(preorder[idx])
            mid = hashed_inorder[preorder[idx]]
            # mid tells us how many nodes sit in the left side of the tree
            root.left = buildTreeWithHash(idx+1, lo, mid-1)
            # removing us from both arrays, and basically passing our whole left subtree
            # without ever passing a node from our right subtree

            # to build the right subtree, we want every value after the left share of the trr
            # in preorder, and the right portion for inorder
            # we do not want to re-consume our root, root is always excluded
            root.right = buildTreeWithHash(idx + 1 + (mid-lo), mid+1, hi)
            return root

        return buildTreeWithHash(0, 0, len(inorder)-1)



         