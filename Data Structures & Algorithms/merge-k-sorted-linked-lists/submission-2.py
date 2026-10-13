# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # ok here, the actual implementation is to run a tree-like 
    # divide and conquer algorithm, that will allow us run our 
    # merges in logk times (k being the number of lists) 
    # sort of in a similar way to mergesort let's implement it 
        if len(lists) == 0 : return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2): # jumping by 2
                pair1 = lists[i]
                pair2 = lists[i+1] if i+1<len(lists) else None
                mergedLists.append(self.mergeList(pair1, pair2))

            lists = mergedLists
    # when we break out of the while loop, we should only have 1 element
        return lists[0]

    def mergeList(self, l1, l2):
        if l1 is None and l2 is None: return None
        elif l1 is None: return l2
        elif l2 is None: return l1
        # both are non-null
        p1, p2, head = l1, l2, None
        if(p1.val < p2.val):
                head = p1
                p1 = p1.next
        else:
            head = p2
            p2 = p2.next
        cur = head
        while p1 != None and p2 != None:
            if p1.val<p2.val:
                cur.next = p1
                p1 = p1.next
                cur = cur.next
            else:
                cur.next = p2
                p2 = p2.next
                cur = cur.next
        # here, either one of the two branches reached its end, or both
        # if one eached it's end, it must mean it was 'walked' at the last
        # iteration and hence, cur is pointed at the last element before
        # None, we should hence point that last .next to whatever is in the
        # remaining list before returnint the head
        if p1 is None and p2 is None : return head
        elif p1 != None : 
            cur.next = p1
            return head
        else:
            cur.next = p2
            return head
            


        