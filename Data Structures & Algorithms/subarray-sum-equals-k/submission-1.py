class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # here the idea is to sort of cache the possible pre-fix array's
        # sum and map them to their count (i.e number of pre-fix arrays)
        # that produce such a value
        # we want to do so in reading order, such that we don't go get 
        # a prefix that is actually a postfix which wouldn't make any sense

        cache = {} # key = pre-fix cuont, value = number of pre-fixes
        # that satisfy it 
        output = 0
        moving_sum = 0 # we'll use this to not re-compute pre-fix sum
        for i in range(len(nums)):
            moving_sum+=nums[i]
            pre_fix_sum = moving_sum
            if pre_fix_sum == k:
                pre = cache.get(0)
                if pre != None:
                    output+=pre # all the zero-summing prefixes
                output += 1 # adding ourselves to the count
                val = cache.get(k)
                if val is None:
                    cache[k] = 1 # then to the cache
                else:
                    cache[k] = val + 1
            else: 
                # first we look for "completing" prefixes, then we 
                # we want sum-prefix = k -> prefix = sum - k
                pre = pre_fix_sum-k
                prefix = cache.get(pre)
                if prefix!=None:
                    output += prefix
                # finally we add ourselves to the cache
                val = cache.get(pre_fix_sum)
                if val is None:
                    cache[pre_fix_sum] = 1
                else:
                    cache[pre_fix_sum] = val + 1
        return output






        