class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # the brute force would be to obviously try every pop every time and would grow
        # in O(n!) which is pretty bad, moreover, we can't memoize on sub-arrays
        # (l, r pointers) as it doesn't guarantee any of the content
        # [4, 2,| 3,5,5,3,2,32,4 |5,6,7] [4 ,2 , 6, 7]
        # actually I think this is a pretty good memoiation as on bigger arrays
        # it may save a lot of repeated compute, now let's just find how to key-it
        # other than hashing the full blown sub-set of values (4, 2, 6, 7)
        # thats very appealing since this sub-set's answer is only true for 
        # that specific ordering is there any other way to hash ?
        # this is the wrong subproblem though as we are caching sub-sequences
        # which grow up to O(2^n)
        #
        # Here we should ask ourselves what would happen if we popped this LAST
        # and hence since it is last, we would be sure that the last mult add 
        # would be 1*num[i]*1 + whatever the rest gave
        # and since it is the last one for the scope of the bigger array
        # we can pass it as final left boundry to whatever we chose to pop
        # as second to last pop (which would hence have 1 to its right and us (i))
        # to its left since we are the true last element
        # we can use pointers to pass down the l and r imaginary boundaries
        # and hence use l-1 and r+1 to know what would be our relative-last's
        # ultimate multipliers and those boundaries will be the key to our cache

        memo = {}

        ## we need to iterate, as caching on i, l, r and using recursion to iterate 
        # over the i's is not good, we'd rather compute the maximum for all is within
        # a boundary and save it as the result for the (l, r) pair

        def rec_search(l, r):
            # i is the last popped (relatively) in l r
            if (l, r) in memo: return memo[(l, r)]
            if l==0:
                left_mult=1
            else:
                left_mult = nums[l-1]
            if r==len(nums)-1:
                right_mult=1
            else:
                right_mult = nums[r+1]
            if l==r: return left_mult * nums[l]* right_mult
            else: 
                best_score = 0 # no negatve values exist
                for i in range(l, r+1):
                    cur_result = left_mult * nums[i] * right_mult
                    left_result = rec_search(l, i-1)
                    right_result = rec_search(i+1, r)
                    result = cur_result + left_result + right_result
                    best_score = max(best_score, result)


                memo[(l, r)] = best_score
                return best_score
        
        sol = rec_search(0, len(nums)-1)
        return sol


        


        