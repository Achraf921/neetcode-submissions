class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # so here, this seems to be a sub-sequence problem, where state should hence 
        # just be i I suppose, the only constraint is that it ends up adding up to
        # the final result, hence maybe the keys could be 
        # position, remainder -> count and hence a knapsack problem
        # which sounds reasonable, let's get to implementation 

        memo = {}

        def memo_knapsack(i, rem):
            if (i, rem) in memo: return memo[(i, rem)]
            if rem == len(t):
                memo[(i, rem)]=1
                return 1 # base case, if we were able to get there, it means we did find a seq
                # to fully consume the t string
            if i>len(s)-1: 
                memo[(i, rem)]=0
                return 0 # how come we reached the end without fully consuming the remainder
            # otherwise we always have two options, take and move, or skip
            # and we don't want to query those greedily
            count = 0
            # take # either it helps or it doesn't
            if t[rem]==s[i]:
                count+=memo_knapsack(i+1, rem+1) # we push both i and rem
            # if taking doesn't build the string we should just skip, but we should also try 
            # skip even if it helps us as skip could yield more paths
            count+= memo_knapsack(i+1, rem) # rem didn't move so we didn't take
            memo[(i, rem)] = count
            return count
        
        return memo_knapsack(0, 0)
            
            
        