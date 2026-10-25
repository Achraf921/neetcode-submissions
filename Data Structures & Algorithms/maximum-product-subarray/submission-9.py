class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # [2, 4 ,-3, -1, 5]
        # scenarios as such break the regular sliding window policy
        # and hence make it a bad choice

        # brute force may be the only available option
        # but it does grow expoenentionally at O(3^n)
        # but some of these sub-arrays do overlap
        # (key word here is some, this is not a very clean memoization case)
        # but I guess this is yet the best bet we can make to improve that 
        # bruteforce solution
        # hence we will cache sub-array (tuples) as keys and their mimimal 
        # sub-array as values to improve that exponential time complexity 
        # into pseudo-polynomial time
        # actually we won't have our keys being tuples but rather 
        # left and right pairs

        memo = {}

        # here actually, after running the memoization with (l, r)
        # as cache key, it did TLE, which makes sense 
        # as getting the exact same l and r is a pretty rare event in our 
        # bruteforce tree, a way to multiplex the data we have to form
        # a more common function call is to cache 
        # a sub-array that runs from beggining to r and one from
        # beginning to l and divides the r one by the l one to get our 
        # l r result, the right sub-array can be reused as nominator 
        # for all divisions and we hence only have to compute l
        # when not in the cache, and inversly which makes
        # fail cases cheaper (as we compute a smaller sub-array product) 
        # let's try to re-implement this

        # again, after implementing this, we noticed that multiplication by 0 in any of the arrays would colapse
        # down the result to 0 and may cause mult by 0 error, hence we may want to 
        # not multiply any zeros and instead store a contains 0 flag such that if used at the numerator 
        # we return zero and if used at the denominator, we just divide by the 0-free version


        # backtracking again, this latter solution is flawed as having both the left and right part having their
        # zero flag raised doesn't tell us much about if the right - left subset does contain a zero 
        # since left is a subset of right, a fix for this would be to store counts of zero
        # if left and right have the same count, then it implies that all of right's zeros are located in the 
        # left area, and if right_zero_count> left_counts it implies that right also has some zeros to it 
        # in the disjoint area and that we should hence retrun 0
        # note that this is the 4th time I backtrack on my solution and that this problem is fucking tricky to 
        # fit, I keep thinkng my tricks are fixing and confidently return them until getting hit by a edge 
        # case and having to expensively backtrack which sucks, but at the same fucking time, I won't get 
        # 2 hours to ponder on all of the missing ramifications of my idea, perhaps am I cooked ?
        # (we will keep zero-counts to figure out what to return)

        # well, well ,well, guess we're backtracking one more time, trying to optimize our 
        # prefix product state approach did provide correctness, but was not TLE free
        # hence here, we may want to double down in the cache by also caching the sub-arrays as we
        # initally did in a double cache setting I guess

        memo_arr = {}


        # btw here, the memo at i does include the element at index i
        def top_down(l, r):
            if l<0 or r>len(nums)-1: return float('-inf') # dead end
            if (l, r) in memo_arr: return memo_arr[(l, r)] # array-level memoization
            if l in memo and r in memo:
                if memo[r][1]==0 or memo[r][1]==memo[l][1]:
                    # in this scenario, we either don't have any zeros or all of right's zeros sit in the left
                    # portion, if the num at l is a zero, multiplying by nums[l] fixes it back to zero, otherwise
                    # it does the intended job of including l in our window
                    result = (memo[r][0]//memo[l][0])*nums[l]
                else: # this means that right has zeros, and more zeros then left, meaning our sub-portion does
                      # contain zeros, and we should hence have our resulting one be zero
                      result = 0
            elif l in memo: # no right
                # we want to compute right from left to save flops since l is a subset or r
                # we want to save the zero-free version of r for caching and count zeros too
                r_zero_count = memo[l][1] # right has all of left's zeros and potentially more
                r_zero_free = memo[l][0]
                l_to_r = nums[l] # will be used to return in case of no-zeros
                for num in nums[l+1:r+1]: # including r, and not counting l twice
                    if num!=0:
                        r_zero_free*=num
                        l_to_r*=num
                    else:
                        r_zero_count+=1
                # we first want to cache the resulting result, and later evaluate it for our compute
                memo[r] = [r_zero_free, r_zero_count] # caching
                if r_zero_count > memo[l][1]: # i.e zeros in our right portion were detected
                    result = 0
                else: # no zeros in our right portion
                    result = l_to_r
            elif r in memo:
                # here we do have r but are missing l, we need to compute left from scratch (0)
                # cache and figure out if our dijoint part contains zeros
                l_zero_free=1
                l_zero_count=0
                for num in nums[:l+1]: # l-including
                    if num!=0:
                        l_zero_free*=num
                    else:
                        l_zero_count+=1
                memo[l] = [l_zero_free, l_zero_count] #caching
                if l_zero_count==memo[r][1]: # i.e all of r's zeros are in l
                    result = (memo[r][0]//l_zero_free)*nums[l]
                else: # r does have some zeros to it
                    result = 0
            else: # we don't have l nor r in cache, we need to compute both
                l_zero_free=1
                l_zero_count=0
                for num in nums[:l+1]: # l-including
                    if num!=0:
                        l_zero_free*=num
                    else:
                        l_zero_count+=1
                memo[l] = [l_zero_free, l_zero_count] #caching

                # continuing from l's work up to r
                r_zero_free= l_zero_free
                r_zero_count= l_zero_count
                l_to_r = nums[l] # for our result
                for num in nums[l+1:r+1]:
                    if num!=0:
                        r_zero_free*=num
                        l_to_r*=num
                    else:
                        r_zero_count+=1
                memo[r] = [r_zero_free, r_zero_count]
                # finally evaluating
                if r_zero_count == l_zero_count:
                    result = l_to_r
                else:
                    result = 0
            
            # now what we have got our result from all possible parts and cached it everywhere that it was possible
            # let's compute the optimal solution
            
             

            optim = max(result, top_down(l-1, r), top_down(l,r+1), top_down(l-1, r+1))
            # let's also cache the optimal solutions respetive to pointers l,r  as it will help memoization I
            # suppose

            memo_arr[(l, r)] = optim

            return int(optim)


        #global_optimal = float('-inf')
        #for i in range(len(nums)):
        #    global_optimal = max(global_optimal, top_down(i, i))
        # probing for every possible 'center'
        #return global_optimal

    # ok even my fully optimized sub_array+prefix memoization based algo didn't cut the stack
    # overflow limit

    # the O(n) version involves Kadan's algorithm which I don't have the heart to type down
    # in comments but I will try to implement down there after getting the idea

        post_fix = [] # format will be sub-arrays [hi, lo]

        for i, us in enumerate(nums):
            if i==0:
                post_fix.append([us, us])
            else:
                # here the previous lo could yeild hi in case of sign filp likewise in the 
                # opposite direction
                us_n_lo = post_fix[i-1][1]*us
                us_n_hi = post_fix[i-1][0]*us
                post_fix.append([max(us_n_hi, us_n_lo, us), min(us_n_hi, us_n_lo, us)]) # hi, lo
        # computing all hi's and lo's at every state of the sub-array
        # (lo is only kept as the next hi may result from lo*us due to sign inversion)
        # and the maxiumum product here is hence the max of the his
        his = [point[0] for point in post_fix]
        return max(his)



        

        