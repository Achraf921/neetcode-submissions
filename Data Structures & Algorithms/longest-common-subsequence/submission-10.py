class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # here a brute force would be to compute all subsequences
        # and then compute all common sub-sequences and then find 
        # the largest
        # and using a dp approach to this brute force would break 
        # as if the largest of both isn't the same, then we would be 
        # left empty handed
        # hence the state we may want to pick is not only the largest 
        # sub-sequence starting at char t[i] but rather a more restrictive 
        # state that also implies that it does also exist in the other string 
        # let's try to think about the base case
        # for array's [t] and [s] for example
        # the longest sub-sequence of t is of len 0 but doesn't exist in our 
        # 2nd array
        # if we maybe grow the array to somehting like
        #.[k,t], [k, s] # we see that a common subsequence is the one starting at k
        # but here we can't walk parallely as both strings may be of different length 
        # or the subsequence may live in different parts of the string (i.e they must
        # not have the same index to be common)
        # hence we need to find a good way to check this
        # now thinking about the whole t2 string and the base case of t1 from the 
        # example, we'd have something like 
        # [t] and [c,r,a,b,t] right, and to verify is the t subsequence also exists in t2
        # we could linear search, 
        # now growing to [a, t], we know that t's largest subsequence would be 1
        # and hence linear searching for a though is not enough, as something 
        # like [c, r, t, a, b] would fit, hence I suppose the state of our 2D DP
        # should hence be [max_len, index] such that we only linear search in the other string 
        # the part previous to that index, and hence, here it would be the [c, r]
        # split which doesn't contain a, and in the initial case it would contain a
        # and hence regressing again to [c,a,t] would have us try t
        # which would have us search fir c in c,r,a,b which would work
        # and have us linear search again but in c, r, a
        # to avoid this hastle, we must hence go from most restrictive to least
        # here finding once the exact index of a in the other string and 
        # checking it against the provided index of the memos of all the possible options
        # which would hence at the end yield something of the order of O(n^2) pseudo 
        # polynomial time which seems to be somehting reasonable for what looks like a 
        # NP-hard problem to me
        # let's try to implement this 

        memo = {} # we want ton have (i_text_1) -> [count, index_in_text2]

        # we'll always run for now the search on text1 and handle edge cases
        # like empty text1 or 2 later

        # we also do need a global, right starting mask, to make sure we don't
        # try to search from characters that have already been claimed
        def memo_search(i, mask):
            nonlocal memo
            if i>len(text1)-1: return 0 # this is our base case
            if (i, mask) in memo: return memo[(i, mask)]
            # we want to linear search for our character's position in string 2 and find the 
            # exact index for this to be O(n)
            ind = -1
            for j in range(mask-1, -1, -1):
                if text1[i] == text2[j]:
                    ind = j
                    break
            if ind==-1: # i,e our char doesn't exist in the othr string hence there is no sequence
            # starting by our character that is common to both
                memo[(i, mask)] = 0
                return 0
            # otherwise we want to work with it, and search for max-sequence
            new_mask = ind # altering mask state for later searches
            max_seq = 0
            # we need a mask for greedy search to always make sense
            for k in range(i-1, -1, -1):
                count = memo_search(k, new_mask)
                if count==0: continue # we don't care about it
                max_seq = max(max_seq, count) # we want to keep the longest
            
            # finally we memoize our answer and return
            memo[(i,mask)] = max_seq+1 # accounting for 1 
            return max_seq+1
        
        if len(text1)==0 or len(text2)==0: return 0 # edge case

        count = 0
        for x in range(len(text1)):
            res = memo_search(x, len(text2))
            if res>count:
                count =res
        return count



