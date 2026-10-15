class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # we lowk want to implement a random Q-learning walking 
        # policy here, and see among the ourputs if our word exists
        # here, the time complexity is also gong to grow at 2^n
        # and we do want a mask to not walk over tiles we've already
        # visited
        # we highkey don't mind about having duplicate characters
        # the word length could also be a character so we should 
        # check everything
        # some string manipulation/hashet solution doesn't work here
        # as walking order needs to hold true

        h, w = len(board), len(board[0])
        sol = []

        def backtracking(path, mask, y, x):
            if x>w-1 or y>h-1: return # we will add later, at every step

            if x==-1 and y==-1: # intialization, we want to start a path
            # at all initialization we want to trigger one path from all 
            # existing cells 

            # we need to add pruning
                for j in range(h):
                    for i in range(w):
                        if mask[j][i]!=False:
                            path+=board[j][i]
                            mask[j][i]=False
                            sol.append(path)
                            if path == word: return
                            backtracking(path, mask, j, i)
                            mask[j][i]=True
                            path = path[:-1]
            else:
                # here we can either go x+1, y+1, x-1, or y-1 if allowed
                if y+1<h and mask[y+1][x] != False:
                    path+=board[y+1][x]
                    sol.append(path)
                    if path == word: return
                    mask[y+1][x] = False
                    backtracking(path, mask, y+1, x)
                    mask[y+1][x] = True
                    path = path[:-1]
            
                if y-1>=0 and mask[y-1][x] != False:
                    path+=board[y-1][x]
                    sol.append(path)
                    if path == word: return
                    mask[y-1][x] = False
                    backtracking(path, mask, y-1, x)
                    mask[y-1][x] = True
                    path = path[:-1]

                if x+1 < w and mask[y][x+1] != False:
                    path+=board[y][x+1]
                    sol.append(path)
                    if path == word: return
                    mask[y][x+1] = False
                    backtracking(path, mask, y, x+1)
                    mask[y][x+1] = True
                    path = path[:-1]

                if x-1>= 0 and mask[y][x-1] != False:
                    path+=board[y][x-1]
                    sol.append(path)
                    if path == word: return
                    mask[y][x-1] = False
                    backtracking(path, mask, y, x-1)
                    mask[y][x-1] = True
                    path = path[:-1]
                        
        init_mask = [[True]*w for _ in range(h)]    
        backtracking("", init_mask, -1, -1)   
        return word in sol 

            
