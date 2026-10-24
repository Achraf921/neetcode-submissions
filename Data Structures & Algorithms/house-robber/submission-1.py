class Solution:
    def rob(self, nums: List[int]) -> int:
        # so here we always have two decisions
        # either rob house at position n and get teleported to n+2
        # (as we can't rob n+1)
        # or skip house at n and get teleported to n+1
        # this is obviously O(2^n) with backtracking and we hence want 
        # to use some form of DP
        # (9, | 8,5,2)
        # here we see that the optimal solution for the sub-array is the
        # one starting at 8, but the optimal one is the sub-optimal
        # + the optimal one from the right part including 9
        # or rather than using optimal and sub-optimal 
        # since this depends on the digits, we can replace optimal by 
        # adjacent and sub-optimal by non adjacent
        # looking at this base case gives us an idea on how we could 
        # solve this DAG by memoizing both the adjacent (i.e the one
        # that did take the left-most house) and the non-adjacent
        # and build up from this
        # let's try to put it into code
        memo={}
        n = len(nums)-1
        def rob_b4_i_rap(k):
            if k>n: return 0
            if k==n: return nums[k]
            if k in memo: return memo[k]

            rob = nums[k]+rob_b4_i_rap(k+2)
            skip = rob_b4_i_rap(k+1)
            # actually if we just memoized one, wouldn't it work ?
            us = max(rob,skip) 
            memo[k]= us
            return us

        return rob_b4_i_rap(0)

        