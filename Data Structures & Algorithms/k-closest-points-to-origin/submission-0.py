class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # we basically want to use a min heap where the value of 
        # our minheap's nodes is based on the distance from origin
        # hence we want to store as [dst, x, y] such that
        # it compares on the 1st element, and since answer is guaranteed 
        # to be unique we should be good

        heap = []

        for x, y in points:
            dst = math.sqrt(x**2 + y**2) # since the origin is 0,0
            heap.append([dst, x, y]) #O(n)
        
        heapq.heapify(heap) # O(n)


        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1:])
        return result
        