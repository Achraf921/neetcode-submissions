# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # one thing I could do is just dump everything into a heap and 
        # then heapsort or do something similar which would run in 
        # O(nlogn) n simply being the number of elements, or just using
        # the build in .sort() function that will also optimize to
        # O(nlogn)

        # however, here, looking at the constraints we do observe that 
        # lists.length is in the [0,10 000] range meaning we could get 
        # up to 10 000 lists, but we also know that the sum of list[i]
        # . length will not exceed 10 000 meaning we are capped at 
        # n <= 10 000 elements, and m (num of list) being free but 
        # linearly related
        # hence we could have 10 000 single-element list
        # whch would spark 10 000 comparaison pointers and run in O(n)
        # to find min and hence doing it 10 000 would trigger O(n^2)
        # compared to insertion of all elements then sorting which 
        # would run in O(n + nlogn) worst case which is much better
        # let's try this out
        r_array = []
        for list_node in lists:
            cur = list_node
            while cur != None: # this just skips if the first node is None
                r_array.append(cur.val)
                cur=cur.next
        # now r_array holds every number
        r_array.sort()
        if len(r_array) == 0:
            return None
        else: # we do have at least one element
            head = ListNode(-67)
            cur = head
            for num, i in zip(r_array, range(len(r_array))):
                if i == 0:
                    head.val = num
                else:
                    cur.next = ListNode(num)
                    cur= cur.next
            return head

        