class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we want to do regular backtracking while
        # keeping our well-former 
        #condition true, since the tokens are unique we will pass a boolean
        # mask, to not grab a token twice
        # as for the bookeeping, we want to keep a count of the 
        # open and closed parenthesis inside our path
        # and a miss-formed sequence for n = 3 such as the following
        # ())()( should be blocked from being created
        # we should not be able to place a parenthesis that could never
        # be closed, or put a closing parenthesis on a path that has none
        # opened like we just did, let's try to code this up

        # since we want to mask, we actually need to generate our array of
        # tokens

        # thiking more about the string building policy, opening 
        # parenthesis should be open-bar, and closing ones are the ones
        # we want to regulate

        tokens = []
        for i in range(n):
            tokens.append('(')
            tokens.append(')')
        sol = []
        def backtrack(path, mask, open_count):
            if len(path) == len(tokens):
                sol.append(path)
                return
            #btw right count will be of the same len as tokens as it is a mask
            # we want to use one un-used token of each kind to make our 
            # paths truly linearly independent
            wasOpenUsed=False
            wasCloseUsed=False
            for tok, i in zip(tokens, range(len(tokens))):
                if wasOpenUsed and wasCloseUsed: break
                if mask[i]:
                    if tok == ')' and open_count > 0 and not wasCloseUsed:
                        path+=(')') #allowed
                        mask[i]=False # to not get dupes
                        backtrack(path, mask, open_count-1)
                        mask[i]=True
                        path = path[:-1] #cleaning behind us
                        wasCloseUsed=True
                        # skipping is fine, a later turn will take it 
                    elif tok == '(' and not wasOpenUsed:
                        # here it kinda is open bar
                        path+=('(')
                        mask[i]=False
                        backtrack(path, mask, open_count+1)
                        mask[i]=True
                        path[:-1]
                        wasOpenUsed=True
            # this should be pretty much it
        backtrack("", [True]*len(tokens), 0)
        return sol






        