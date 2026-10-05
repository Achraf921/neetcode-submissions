class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we'll use a hashset to first walk the list and put
        # all elements in, and then for every element, we'll
        # keep querying for n+1 and see if it exists, holding
        # a local length for the consecutive string of nums
        # and replacing the global one if it exceeds it in lenght
        cache = set()
        global_longest = 0 # inital should be zero
        for i in nums:
            cache.add(i)
        
        for i in nums:
            longest = 1
            next = i+1
            while True:
                if next in cache and i + global_longest in cache:
                    # this is highkey a trick to make sure we 
                    # don't wast time on consecutive sequences 
                    # that won't even be a global longest
                    # but it is not consisten as we could have the 
                    # i + global_longest element in cache but 
                    # elements in the middle could be missing
                    longest+=1
                    next+=1
                else:
                    break
            if longest>global_longest:
                global_longest = longest
        return global_longest