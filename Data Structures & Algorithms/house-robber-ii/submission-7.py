class Solution:
    def rob(self, nums: List[int]) -> int:
        # I guess we are here faced with the same dilema
        # of either robbing and moving to n+2 or skipping 
        # and moving to n+1
        # but now our first 'step' also conditions our last 
        # one here I guess
        # for instance, imagining we had a [2,3,2,4] neighborhood
        # taking at 2 would mean that if we ever reached 
        # end -1 we'd have to take or skip but not rob
        # I still think we are in a sort of DAG setup 
        # where top-down memoization and later bottom 
        # up tabulation would work so let's try to pull it off
        # keeping track of the constraint (we'll try to pass it
        # as an arg)

        memo = {}
        n = len(nums)-1

        # ouuh shi, it is actually 2D memoization we can't memoize the 
        # True and false ones the same
        def rec_rob(k, take):
            nonlocal memo
            if k == n:
                if take: return 0 # we can't take
                else: return nums[k] # optimal if we can rob
            if k>n: return 0
            if (k,take) in memo: return memo[(k,take)]
            # special case for k==-1 which will be our initializer
            if k==0:
                rob = nums[k]+rec_rob(k+2, True)
                skip = rec_rob(k+1, False) # skipped openner
            else:
                rob = nums[k]+rec_rob(k+2, take)
                skip = rec_rob(k+1, take)
            result = max(rob, skip)
            memo[(k,take)]=result
            return result
        # let's see if it works

        return rec_rob(0, False)

                
        
        