class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # here the brute force would simply require scanning all of the list 
        # query times, however we can have up to 100 000 queries which 
        # pushes us towards log(n) time for querying which pushes us towards 
        # a heap, now the question we may want to ask ourselves is on what
        # should we run the min heap (i.e en which value) that would allow
        # us to cheaply know if an interval

        heap = []
        intervals.sort(key=lambda x: x[0]) # sorting on 1st key
        i=0
        # to always pop from the same heap we also need to sort the queries while maintianing the
        # order such that we always pop for the latest ones first
        augmented_queries = [[q, k] for k,q in enumerate(queries)]
        augmented_queries.sort(key=lambda x: x[0]) # sorting on the time
        solution = [0] * len(queries)
        for query in augmented_queries:
            while i<len(intervals) and intervals[i][0]<=query[0]:
                heapq.heappush(heap, [intervals[i][1]-intervals[i][0]+1,intervals[i][1]])
                i+=1
            # once we've found the first element who'se start
            # we pop without ever pushign back since the queries are sorted by time
            # and we push them to their right index in solution
            target = query[0]
            result = -1
            while len(heap)>0:
                cur = heapq.heappop(heap)
                if cur[1]>=target:
                    result = cur[0]
                    heapq.heappush(heap, cur) # putting it back as the next one might be equal to us
                    break
            solution[query[1]] = result
        return solution
        