# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        local_head = None
        local_tail = None
        global_cur = head # we create this for consistency
        #purposes
        while True:
            cur = global_cur
            for _ in range(k):
                stack.append(cur)
                cur=cur.next
                if cur is None : break
            saved_next = cur # useful for later advencing

            if len(stack) == 0: return local_head
            elif len(stack) >= k:
                new_head = stack.pop()
                cur = new_head # recycling cur pointer

                while len(stack)>0:
                    cur.next= stack.pop()
                    cur = cur.next
            else: # smaller than k scenario
                # elements in the stack are already in the righ torder
                new_head = stack[0]
                cur = stack[-1]

            if local_head is None:
                local_head = new_head
                local_tail = cur
                global_cur = saved_next # first_element of next batch
                local_tail.next = None
            else: 
                local_tail.next = new_head
                local_tail = cur
                local_tail.next=None
                global_cur = saved_next
            
            if global_cur is None: return local_head
            





        