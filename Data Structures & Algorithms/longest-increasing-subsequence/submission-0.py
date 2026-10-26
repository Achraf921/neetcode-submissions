class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # this is quite intuitively a DAG problem as a sub sequence's 
        # pre-fix has for length the one of the subsequence +1
        # this almost feels like topological sorting 
        # as we just need the longest topological sorting
        # let's try to build an adjacency list and see where this takes us
        # well here, building an adjacency list would actually be pretty expensive
        # O(n^2) we may want to just try memoization first top-down

        # the state we want to keep I suppose should be the number of subsequent
        # values for a number
        memo = {}
        

        def memoized_search(i):
            if i>=len(nums)-1: return 0
            if i in memo: return memo[i]

            # otherwise, we lowkey want to take the max of all elements that 
            # follow us 
            predecessors = 0
            for k in range(i+1, len(nums)):
                if nums[k]>nums[i]: # strict
                    predecessors = max(predecessors, 1+memoized_search(k))

            memo[i] = predecessors # memoize
            return predecessors

        result = 0
        for j in range(len(nums)):
            result = max(result, 1+memoized_search(j))

        return result

            
            
            
        