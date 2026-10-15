class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # so here, this seems to be a problem where we're backtracking
        # all queen's possible solutions, building 
        # row by row or column by column, 
        # ofc the constraints made on our choices is that we must not put 
        # we need to pass the sort of "banned columns",
        # but a smarter way to do so is just to pas in the right order
        # the horizontal (x) position of each queen such that we know 
        # which column is off, and we get to compute the stride of that 
        # queen's diagnoal in function of which row we are at
        sol = []
        def backtrack(pos, stack):
            if pos == n+1:
                print(stack)
                sol.append(stack.copy()) #i.e our board
                return

            # we will be working in 1-index here for easy math
            banned_positions = set() # at our curren row i
            for q, dj in zip(stack,range(len(stack))):
                j = dj+1
                banned_positions.add(q)
                right_diag = q+abs(j-pos)
                left_diag =  q-abs(j-pos) # diag computations
                if right_diag<=n: banned_positions.add(right_diag)
                if left_diag>=1: banned_positions.add(left_diag)
            for x in range(n):
                if (x+1) not in banned_positions:
                    stack.append(x+1)
                    backtrack(pos+1,stack)
                    stack.pop()
                
            
        def stack_to_board(stack):
            out = []
            for num in stack:
                string = ""
                for j in range(n):
                    if j+1 == num:
                        string+="Q"
                    else:
                        string+='.'
                out.append(string)
            return out # this produces an array per stack of number

        backtrack(1, [])
        #print(sol)
    
        array_of_strings = [stack_to_board(stack) for stack in sol]
        #print(array_of_strings)
        return array_of_strings



        