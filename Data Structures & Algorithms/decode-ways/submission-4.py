class Solution:
    def numDecodings(self, s: str) -> int:
        # this is actually climbing stairs/DP problem as the way we count 
        # depends on where our pointer sits/is not uniform

        # let's first try to do it in a top down way to see which relationship
        # we need to tabulate

        memo = {}

        # we just want an edge case handling for single char inputs as they break
        # our function

        if len(s)==1:
            if s[0]=='0': return 0
            else : return 1
        if s[0] == '0': return 0

        # we'll want to return a pair with a boolean flag to signal that a 
        # 'forbidden' sequence happened somewhere (poisoning)
        def top_down(i):
            if i>=len(s)-1: return 1, True
            # base case, doesn't add any ways of counting
            if i in memo: return memo[i], True

            # now let's compute both the take and skip scenarios
            # take: we can only take the next char if we are 1 or 2 and 
            # the next one is in the proper ranges
            take = 0
            if s[i] == '1':
                take_res =  top_down(i+2)
                if not take_res[1]:
                    return -1, False
                take = take_res[0]
            if s[i] == '2': # take only exists if we can
                num = int(s[i+1])
                if num<7:
                    take_res =  top_down(i+2)
                    if not take_res[1]:
                        return -1, False
                    take = take_res[0]
             # if not, possible we are constrained to not take and skip
                # and hence the take path remains 0
            
            # skip, we just take our number (if allowed to)

            skip = 0
            if s[i]=='0': # this one doesn't count, we hence need
                if s[i+1]== '0': # no need to keep going and we can just poison
                    return -1, False
            # otherwise we don't want to count it as a path

            # otherwise we can always take our char as a number 
            elif s[i+1]!='0': # if it were zero, we wouldn't be allowed to skip 
            # and only option would be to take the 0 with us
                skip_res = top_down(i+1)
                if not skip_res[1]:
                    return -1, False
                skip = skip_res[0]

            result = take+skip
            memo[i]= result

            return result, True # if we passed all of the previous results
        
        final_result = top_down(0)
        if not final_result[1]: return 0
        else: return final_result[0]

        

            
                
            
