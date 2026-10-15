class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # ok so we want to cut the string, and backtrack if that cut doesn't
        # yield anything, and when we append, we want to return rather than 
        # appending infinitely to that bucket
        # we basically want to try all splicing of the string that do hand a 
        # palindrom on one side, if none yield, then we go for char

        sol, path = [], []

        def backtrack(start):
            if start == len(s):            # whole string is cut
                sol.append(path.copy())    # path IS one bucket
                return
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if piece == piece[::-1]:   # only cut off palindromic prefixes
                    path.append(piece)
                    backtrack(end)         # cut the rest
                    path.pop()

        backtrack(0)
        return sol



            
        