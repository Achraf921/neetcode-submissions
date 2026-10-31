"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0: return 0
        elif len(intervals)==1: return 1
        intervals.sort(key = lambda x: x.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)# end time occupancy
        for inter in intervals[1:]:
            cur = heapq.heappop(heap)
            if cur>inter.start: # i.e we do overlap
                heapq.heappush(heap, cur)
                heapq.heappush(heap, inter.end) # basically adding a new room
                # and always returning the one with the earliest occupancy
            else: # no overlap, we don't push cur back and just push our own 
            #occupancy as it is above cur's
                heapq.heappush(heap, inter.end)

        return len(heap)
        