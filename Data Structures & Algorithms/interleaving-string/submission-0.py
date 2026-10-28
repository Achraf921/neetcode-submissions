class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # how could we not interleave a string correctly when mixing them ?
        # let's say we have abcde, and fg
        # if I go a , (f), [b], (g), [c, d, e]
        # then despite the ssize difference, we still have the same number of substrings
        # from each of the two string
        # maybe the condition is that all substring have to be of same length ?
        # but this is not mentined anywhere, hence our interleaving of the two strings
        # should be correct right ?
        # and hence if all mix are interleaves, then wouldn't
        # just appending them and sorting both s1+s2 and s3 tell you if they get to 
        # the same result ?
        # I don't see how this could ever go wrong (and if not of the same lenght, return false
        # before even sorting)
        # if I have two strings, aaaaaaaaaaaaaaaa, and b
        # then I can either interleaf as, baaaa.... which has n = 1 and m = 1, aaa...b has the same
        # and aaabaaaa... # has n = 2 m =1 which fits
        # on the other hand, for aaaaa bbbbb, how could we built something that breaks the 
        # interleaf criteria (btw NOWHERE it is mentioned that all substrings must be of 
        # the same length right ?)
        # well aaa b aa bbbb fits, so does a b a b a b aa bb, ect, this is almost provable by 
        # this almost sounds like it could be proven by recursion so I have very strong 
        # reasons to think that either the problem definition is ambiguous/doens't state 
        # that all substring lengths must be of equal lenght (which hence disqualifies
        # any string of odd lenght, which is weird (or makes us sit it as a monolith))
        # or I may perhaps have missread the problem
        # after re-reading, the only additional constraint is that the order must be 
        # maintained which indeed swipes off a sorting solution, and hence
        # probably makes us go towards some DP solution
        # since we have to keep order, this is probably some knapsack DP
        # where we only get to look ahead of our position (exclusive)
        # and the state is whatever is remaining of the string
        # and we get to pick from both pools, hence I suppose making it a 3D DP
        # solution knapsack, i.e ((x, y), remainder) -> can_build_to_remainder
        # let's try to implement this

        memo = {}
        # x will be for s1 and y for s2
        
        if len(s1) + len(s2)!= len(s3): return False
        if s1=='' and s2=='' and s3=='': return True

        # btw just noticed this is actually 2d, as to compute the remainder, we could 
        # just compute the len of x and y and see if the character sitting at x+y+1
        # matches any of our x or y extensions

        def knapsack(x, y):
            if (x, y) in memo: return memo[(x, y)]
            if x==len(s1) and y==len(s2): # end was reached
                memo[(x, y)] = True # this will only be reachable if we did find a combo
                return True


            # otherwise we need to make a couple choices
            # first of all, we NEED to pick a next char, as s1 + s2 = s3 
            # implies that our resulting interleaving is of same len as s3
            # hence everything must be consumed
            # now we cannot consume past one's index, and we cannot consume a character that
            # doesn't meet the target

            result = False
            
            if x<len(s1) and s1[x]==s3[x+y]: # this is potentially a good fit
                result = result or knapsack(x+1, y) # truncating
            
            if y<len(s2) and s2[y]==s3[x+y] and not result: # we could potentially try both
                result = result or knapsack(x, y+1)
            
            memo[(x, y)] = result
            return result

        return knapsack(0, 0)

        