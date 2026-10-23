class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # negative for max heap

        heap = [-k for k in nums]
        heapq.heapify(heap) #O(n)

        result = -1
        for i in range(k):
            if i == k-1:
                result = heapq.heappop(heap)
            else:
                heapq.heappop(heap)
        
        return -result


        