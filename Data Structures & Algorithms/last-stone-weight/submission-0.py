class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # run heap till left with one elements

        heap = [-s for s in stones] # negative values to have a max heap
        heapq.heapify(heap)

        while len(heap)>1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x==y: continue
            else:
                mx = max(x,y)
                mi = min(x,y)

                heapq.heappush(heap,-(mx-mi))
        
        if len(heap)==0: return 0
        else: return -heapq.heappop(heap)
        