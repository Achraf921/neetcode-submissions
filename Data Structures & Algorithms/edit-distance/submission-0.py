class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # the insert and replace parts make it worst as we need some policy to 
        # decide rather than just trying to insert all 26 letters of the 
        # alphabet, same for replace, delete is sort of a skip where 
        # we don't take the character

        # here are the actual options in backtracking fashion:
        # take and move on (replace, by ourselves)
        # skip (delete)
        # insert (add, not a usual option, could lead to an infinite process)
        # replace not by ourselves (also un-usual)
        # to get the optimum, the bruteforce would indeed be to try everything
        # but insert without a restriction would lead to infinite recursion
        # hence, for two non-overlaying strings:
        # abcd, efgh, there is no scenario where inserting doesn't lead to deleting 
        # and hence worsens, hence we should only allow to insert if the target
        # is larger then us

        # monkeyyyyyyyyy ey
        # monkeyyyyyyymon ey
        # money

        # I feel like this could be a 2D knapsack where we want the sub-string to 
        # match the remainder in a minimum amount of moves, and we only want to insert
        # the right character, if the end is reached without success, hence 
        # there is no failure scenario, just bad move counts, and we want to store as
        # state the best counts, let's try to put this into code

        # and the worst case scenario here at equal lenght should be replace at every
        # position, hence the only scenario where we'd reach the end without
        # finding a solution would imply that either we went down a bad path
        # or that the word2 string is larger
        # and delete is sort of the anti-insert, and should only be used 
        # when word1 is larger than word2

        memo = {}

        def weird_knapsack(i, rem):
            if (i, rem) in memo: return memo[(i, rem)]
            if i>=len(word1) and rem<len(word2): # i.e if we still have a remainder
                # only thing we should do is insert
                # and we could use i to count the number of extra inserts we did
                # we must add the delta which costs the delta
                result = (len(word2)-rem) # eq to inserting the missing char sort ofs
                memo[(i, rem)] = result
                return result
            if rem>=len(word2) and i<len(word1): # we must delete, as we were able to fully consume
                result = len(word1)-i # we must delete the delta, which costs the delta
                memo[(i, rem)] = result
                return result
            if rem>=len(word2): # i.e we fully consumed the remainder
                memo[(i, rem)] = 0
                return 0
            

            
            min_moves = float('+inf')
            if word1[i] == word2[rem]: # if equal, we greedily take
                min_moves = min(min_moves, weird_knapsack(i+1, rem+1)) # free move
            else:
                # we could either delete if too long or replace and delete later which 
                # is lowk equivalent count wise, but delete could bring in good chars
                # and is kinda like a paid-for skip
                # del:
                min_moves = min(min_moves, 1+weird_knapsack(i+1, rem))

                # when using replace, we obviously want to replace with a matching character
                # which hence this time advances the remainder
                # kinda like a paid for take
                # replace :
                min_moves = min(min_moves, 1+weird_knapsack(i+1, rem+1))

                # trying insert can also sometimes help us
                min_moves = min(min_moves, 1+weird_knapsack(i, rem+1))

            memo[(i, rem)] = min_moves
            return min_moves

        return weird_knapsack(0,0)










        