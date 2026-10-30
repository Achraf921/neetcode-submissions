class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals)==0: return [newInterval]

        # [1,8],[2,3] [10,19] | -> [1, 19]
        right_neigh = -1
        counter = 0
        result = []
        while counter < len(intervals):
            if intervals[counter][0]>newInterval[0]:
                right_neigh=counter # thats the spot we want to take
                break
            else:
                result.append(intervals[counter])
                counter+=1
        
        # now we want to check for overlap and if we sit at an edge of the array
        left = newInterval[0]
        right = newInterval[1]
        starterRight = right_neigh
        if counter>0:
            if right_neigh==-1: i=0 # such that the -1 works fine at getting the very 
            else: i=right_neigh
            left_bound = intervals[i-1][1]
            if left_bound>=left: # we want to merge with the left side
                left = intervals[i-1][0] # we know for sure this is the smallest left
                right = max(right, intervals[i-1][1]) 
                # that means we've merged and we hence want to pop our left neighboor
                result.pop()
            
            
        #! it can happen that we merge both left and right btw
        if right_neigh!=-1: # i.e if we do have a right neighbor
            merging = True
            while merging:
                if right_neigh < len(intervals) and right >= intervals[right_neigh][0]:
                    # here left doesn't change since we're guranteed to win
                    right = max(right, intervals[right_neigh][1])
                    # we now also want to pop 
                    right_neigh+=1 # we want to test against the next right neighboor
                    starterRight+=1 # to skip our right neighboor since it is merged onto us
                else:
                    merging = False # since non-overlapping it should be capped
        
        result.append([left, right])
        if starterRight!=-1 and starterRight<len(intervals): # since there would be nothing to append
            for k in range(starterRight, len(intervals)):
                result.append(intervals[k])
        return result
            