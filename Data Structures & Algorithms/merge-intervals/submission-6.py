class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # quick helper
        def merge_em(interval1, interval2):
            return [min(interval1[0], interval2[0]),max(interval1[1],interval2[1])]

        intervals.sort(key= lambda x: x[0])
        res = []
        i=0
        while i <len(intervals):
            cur = intervals[i]
            after = intervals[(i+1)%len(intervals)]
            if i<len(intervals)-1 and cur[1]>=after[0]: # the very last has nothing to merge with
                # we know it overlaps AT LEAST with this one but may want to walk
                # all the way before appending
                cur = merge_em(cur, after)
                k = i+2
                while k < len(intervals):
                    if intervals[k][0]<=cur[1]:
                        print(cur)
                        cur = merge_em(cur, intervals[k])
                        k+=1
                    else:
                        break
                res.append(cur)
                i=k
            else:
                res.append(cur)
                i+=1
        return res

        