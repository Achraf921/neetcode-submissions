# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # no left node at all seems like an edge case ! to consider

        # this looks a whole lot like a in-order dfs that goes left
        #                  count, solution
        def k_dfs(count, node) -> (int, int):
            #left
            if node.left is None and node.right is None:
                if count == -2:
                    return (1, node.val)
                else:
                    return (count+1, node.val)
            if node.left is not None:
                count_left, sol_left = k_dfs(count, node.left)
                if count_left == k or count_left == -1:
                    return (-1, sol_left)

            #in-order
            # there is a single scenario where a middle node is first, 
            # and it is when the count is -2 AND the right child no left child


            if count == -2 and node.left == None:
                count = 1
                if k == count:
                    return -1, node.val
            elif node.left == None and count!=-2:
                count+=1
                if k == count:
                    return -1, node.val
            elif node.left is not None: # we do have a left child
                count_left+=1 # since it will be the one count used by right
                if k == count_left:
                    return (-1, node.val)


            # right
            if node.right is not None:
                if node.left is not None:
                    count_right, sol_right = k_dfs(count_left, node.right)
                else:
                    count_right, sol_right = k_dfs(count, node.right)
                if count_right == k or count_right == -1:
                    return (-1, sol_right)

            # fall through scenario :
            # none of our children sits at the right count
            # we need to watch our for which count we return
            # we also need to check if WE are not the expected return val
            # this is useful if the node we are looking for 
            # happend to be the root and has hence no children that will 
            # query it and check
            if node.right is not None: 
                # either only right or both children
                return (count_right, node.val)

            elif node.left is not None: 
                # we only have left
                return (count_left, node.val)
            else:
                raise RuntimeError("no children ? sounds like an indentation pb")
            
        _ , sol = k_dfs(count=-2, node=root)
        return sol
        