# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # we sort of want breadth first search right, but where
        # instead of consuming nodes one by one off the main queue,
        # we want each time to completely flush it empty
        # and store the nodes we've got while flushing in a secondary 
        # queue
        # 1, 2, 3, 4, None, 6, 7
        # we return when both queues are fully emptied

        main_queue = deque()
        sec_queue = deque()
        return_array = []
        if root is None: return [] # empty guard
        main_queue.append(root)
        while len(main_queue)>0:
            sub_return_list = []
            while len(main_queue)>0: # until fully flushed, we keep going
                e = main_queue.popleft()
                sub_return_list.append(e.val)
                if e.left is not None:
                    sec_queue.append(e.left)
                if e.right is not None:
                    sec_queue.append(e.right)
            return_array.append(sub_return_list)
            main_queue = sec_queue # make the main queue the secondary q
            sec_queue = deque()

        return return_array

        # time complexity : O(n)
        # space complexity : O(n/2) 

