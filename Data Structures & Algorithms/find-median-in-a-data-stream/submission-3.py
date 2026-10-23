# here we have a lot of calls, fingind the meadin is quite easy O(1), it is the 
# insertion part that is usually O(n), a heap makes insertion O(logn), but at 
# the cost of losing ordering as it is tree-based
# the question hence becomes how to insert cheaply while keeping ordering

# here the trick is to cut the array into two halves, store them as a max heap
# for the left and a min heap for the right, and use those two to find out
# the median


class MedianFinder:
    def __init__(self):
        self.left = [] # max_heap
        self.right = [] # min_heap
        self.len_left = 0
        self.len_right = 0
        

    def addNum(self, num: int) -> None:
        # base case, we insert left
        if len(self.left)==0 and len(self.right)==0:
            heapq.heappush(self.left, -num)
            self.len_left+=1
        else:
            left_max  = -self.left[0]
            right_min =  self.right[0] if self.right else float('-inf')
            if self.len_left==self.len_right:
                if num<=left_max:
                    heapq.heappush(self.left, -num) # negative to get max-heap
                    self.len_left+=1
                else: # when larger than the max left element
                    heapq.heappush(self.right, num) # negative to get max-heap
                    self.len_right+=1
            else: # here is the tricky part, we want to keep balance
                if self.len_left>self.len_right: # largest delta ever should be one
                    # either the element belongs right, and we just insert it there
                    # or if it belongs left we need to trade one left element to the
                    # right and then insert left
                    if num<left_max: #i.e it belongs left, we need to trade
                        max_left = -heapq.heappop(self.left) # negative initially
                        heapq.heappush(self.left, -num) #inserting the num
                        heapq.heappush(self.right, max_left) # finally balanced
                    else: # it belongs right, and there is no issue
                        heapq.heappush(self.right, num)
                    self.len_right+=1 #incrementing right by 1 in both cases
                else: # right heavy, symetric question as from the last one
                    if num > right_min: # it belongs right and we must trade
                        min_right = heapq.heappop(self.right)
                        heapq.heappush(self.left, -min_right) # neg for min heap
                        heapq.heappush(self.right, num)
                    else: # it belongs in left fine
                        heapq.heappush(self.left, -num)
                    self.len_left+=1 # in both scenarios


            
    def findMedian(self) -> float:
        # this should happen in O(1), 
        if self.len_left == self.len_right: # balanced/even length
            left = -heapq.heappop(self.left) # back to positive since max heap
            right = heapq.heappop(self.right)
            heapq.heappush(self.left, -left)
            heapq.heappush(self.right, right)
            return (left+right)/2
        else: # odd, left heavy, hence we just need the max element from left
            if self.len_left>self.len_right:
                left = -heapq.heappop(self.left) # back to positive since max heap
                heapq.heappush(self.left, -left)
                return left
            else:
                right = heapq.heappop(self.right)
                heapq.heappush(self.right, right)
                return right

        
        