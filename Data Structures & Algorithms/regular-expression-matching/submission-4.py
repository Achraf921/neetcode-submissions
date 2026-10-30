class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # ok this is actually not greedy territory nor trie territory
        # especially for the x* tokens, we need to find out 
        # how many of my characters I should pick to not break the regex (if it was
        # correct as picking the wrong number of chars would fail us)
        # this hence creates a k-choice branching at every x* going from skip
        # to grabbing all of the x chars after us
        # this brute force would actually work and if it were ever to yeild an
        # existing solution would work
        # but a string containing many x** or only those would grow to exponential time
        # we hence need a way I suppose to cache whenever those arise the state
        # what we could save is is subtring starting from i regex-friendly
        # but the thing is that somethimes it is the n** that will make it fit inside 
        # of our regex so trying to do a knapsack here would fail I suppose
        # nnnnnnnjnnnnjnjjnnnnjjjnn
        # n*nnn.nnn*knz*njjnnnnn*jjj*n*
        # how to visualize solving this as a DAG though, what should be the sub-problem
        # and more importantly, why would knapsack fail ? if I walk left to right, stopping
        # at my first * expression, yeah, the number I need to take also lowkey depends
        # on what is left of me, how to actually break this into sub-problems ?
        # maybe what we could do is push our left pointer on the check string to the left-
        # most possible n here, and hence try, but we would need to take into account
        # how many n's come before and after our n* too
        # I suppose the unit of the sub-problem may be centered around this
        # but this also breaks as we need to make the dots (.) correctly align 
        # by hence taking the exact right number of n's
        # let's try some reverse thinking here and see if we can not go from the 
        # to-be-checked string and


        # let's just try to implement the brute force
        # i walks the string we want to match, j walks the regex

        memo = {}
        def brute_walk(i, j):
            if (i,j) in memo: return memo[(i,j)]
            if j==len(p):
                return i==len(s)
            if j<len(p)-1 and p[j+1]=='*':
                # we either take and not move, skip or take and move
                result = False
                if i<len(s) and (p[j]=='.' or p[j]==s[i]):
                    result = result or brute_walk(i+1, j) # not move and take
                result = result or brute_walk(i, j+2) # move and not take
                memo[(i,j)] = result
                return result
            if p[j]=='.' and i<len(s): # we just add whatever is currently available
                result = brute_walk(i+1, j+1)
                memo[(i,j)] = result
                return result
            elif i<len(s):
                if p[j]!=s[i]: 
                    memo[(i,j)] = False
                    return False
                else:
                    result = brute_walk(i+1, j+1)
                    memo[(i,j)]= result
                    return result

            memo[(i,j)] = False
            return False # wtf

        return brute_walk(0,0)

        