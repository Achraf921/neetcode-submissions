class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        my_nums = [-n for n in nums] # negative values for reverse ordering
        heapq.heapify(my_nums)
        self.heap = my_nums
        self.k = k
        

    def add(self, val: int) -> int:
        print(self.heap)
        heapq.heappush(self.heap, -val)
        buff = []
        for _ in range(self.k):
            buff.append(heapq.heappop(self.heap))
        returned = -buff[-1] 
        for n in buff:
            heapq.heappush(self.heap, n) # n is alr negative
        return returned

        
