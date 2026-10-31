class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        count=0

        # [1, 4], [2,99], [3, 10], [11, 121]
        
        # here this is a greedy algorithm and the heuristic is just to ALWAYS remove (when
        # faced with overlappig intervals the one that ends first)
        i=1
        cur = intervals[0]
        while i < len(intervals):
            after = intervals[i]
            if cur[1]>after[0]: # we want to remove the one with the smalles right bound
                if cur[1]<after[1]:
                    cur = cur
                else:
                    cur = after
                 # skipping the next one as we removed it
                count+=1
                i+=1
            else:
                cur = after
                i+=1
        return count

            

