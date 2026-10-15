# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None: return "[]" # edge case
        # first let's get max depth through a DFS helper
        def depth_dfs(node):
            if node is None: return 0
            left, right = 0, 0
            if node.left is not None:
                left = depth_dfs(node.left)
            if node.right is not None:
                right = depth_dfs(node.right) 
            return max(left,right)+1
        max_depth = depth_dfs(root)
        output = "["

        # btw when using this, we'd want to init with depth 1
        # this is a BFS btw
        queue = deque()
        queue.append((root, 1)) # tuple : (node, depth)
        while len(queue)>0:
            # we may want to have some None elements in our queue
            # for ordering purposes, hence we will need to review 
            # our condition
            cur = queue.popleft()
            if cur[0] is not None:
                output+=(f'{cur[0].val},')
                if cur[1] == max_depth:
                    # if we are at max depth we don't append None s
                    continue
                else:
                    if cur[0].left is not None:
                        queue.append((cur[0].left, cur[1]+1))
                    else:
                        queue.append((None, cur[1]+1))
                    if cur[0].right is not None:
                        queue.append((cur[0].right, cur[1]+1))
                    else:
                        queue.append((None, cur[1]+1))
                    # we will use this count for O(1) termination
            elif cur[0] is None:
                output+=('null,')
                # we don't do anything further
        print(output[:-1]+']')
        print(max_depth)
        return (output[:-1]+']') # cutting last comma
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '[]': return None # edge case
        # here the kind of math we'd want to 
        # do with something like a heap can't 
        # be done as we have a compact serialization
        # let's rather use BFS
        i = 0
        our_data = data[1:-1]+','

        def mint_token(): # we'll use this helper to consume
            nonlocal i
            string = ''
            while our_data[i]!=',':
                string+=our_data[i]
                i+=1
            i+=1 # moving to beg of next string for next iteration
            if string == 'null': #i.e it is a none
                return None
            elif string != '':
                return (int(string)) 

        # now we want to use BFS
        # but we lowk want to fill our queue first
        arr = []
        while i<len(our_data):
            tok = mint_token()
            if tok is None:
                arr.append(None)
            else:
                arr.append(TreeNode(tok, None, None))
        # now let's get to popping
        queue = deque() #our elements are element, idx 
        queue.append(arr[0])
        head = None
        idx = 0
        while len(queue)>0:
            cur = queue.popleft()
            left, right = None, None
            if idx+1<len(arr):
                left = arr[idx+1]
            if idx+2<len(arr):
                right = arr[idx+2]
            if left is not None:
                cur.left = left
                queue.append(left)
            if right is not None:
                cur.right = right
                queue.append(right)
            if head is None:
                head = cur
            idx+=2
        return head
            

            


            




