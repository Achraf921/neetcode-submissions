class Solution:
    def jump(self, nums: List[int]) -> int:
        # this is definitely a backtracking problem
        # we want to log the number of jumps each cell uses to get to the end
        # and since we assume that there is always a valid answer, this shouldn't be 
        # too hard to do with memoization

        memo = {}

        # state is simply cell i -> jumps, we want to try all of the cells right to 
        # us in our jump range

        def track_n_memo(i):
            if i in memo: return memo[i]
            if i>=len(nums)-1:
                return 0 # base case
            
            # otherwise we just want to try all of the cells right to us in a greedy fashion
            # and keep the min of them

            min_jump = float('+inf')

            for jump in range(i+nums[i], i, -1): # it is ok to go till i-1 since we assume it 
            # always has a solution
                min_jump = min(min_jump, 1+track_n_memo(jump))
            
            memo[i] = min_jump
            return min_jump
        
        return track_n_memo(0)

        