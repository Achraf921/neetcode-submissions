"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        for k in range(len(intervals)-1):
            cur = intervals[k]
            after = intervals[k+1]
            if cur.end>after.start: return False
        return True

