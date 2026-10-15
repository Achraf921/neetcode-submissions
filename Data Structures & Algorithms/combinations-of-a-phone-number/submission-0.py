class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        sol = []
        # easy one this time
        our_dict = [[], ['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l', ], ['m','n','o'],['p','q','r','s'], ['t','u','v'],['w','x','y','z']]

        def backtracking(path, i):
            if len(path) == len(digits):
                sol.append(path) # string so no copying
                return
            
            for c in our_dict[int(digits[i])-1]: # getting all the possible chars
                backtracking(path+c,i+1)
            
        backtracking('', 0)
        return sol

            
        