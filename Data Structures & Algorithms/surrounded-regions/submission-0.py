class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # here we may want to grab every O first (it's position)
        # then arbitrarly run BFS on the first one, if it is an island, 
        # we'll want to set all of its O's to X's, and if not
        # we'll want to just set them to false in the boolean mask

        h, w = len(board), len(board[0])

        mask = [[False]*w for _ in range(h)] # has it already been walked ?

        # we'll be using a flag, to signal if the sides were ever reached
        # but last missing piece is how to sort of "walk-back"
        # everything, brute force thought is to dumb everythign into a bin
        # and then if it was indeed an island, flip all of those to 
        # X in O(island_area), this should not take is to O(n*m ^ 2 )
        # territory so I'll judge it suffient, and maybe try to backtrack on 
        # it later if I have some time

        # let's grab all Os
        all_os = deque()
        for j in range(h):
            for i in range(w):
                if board[j][i]=='O':
                    all_os.append([j,i])
        
        # now that we have all Os, we want to arbitratly bfs on them, with the flag and bin

        while len(all_os)>0:
            y, x = all_os.popleft()
            if board[y][x]!='O' or mask[y][x]:
                continue
            # else we do want to run BFS from there, with our flag and bin
            has_touched_border = y==0 or y==h-1 or x==0 or x==w-1
            my_island = [[y,x]]
            mask[y][x] = True
            local_q = deque()
            local_q.append([y,x])
            while len(local_q)>0:
                y, x = local_q.popleft()
                for j,i in [[-1,0],[1,0],[0,-1],[0,1]]:
                    yk, xk = y+j, x+i
                    # we want to border check to flip our boolean, but to keep the BFS going
                    # such that we grab all elements of that water-touching island
                    if yk>=0 and yk<h and xk>=0 and xk<w and not mask[yk][xk] and board[yk][xk]=='O': 
                        if yk==0 or yk==h-1 or xk==0 or xk==w-1: #neighboor's position on the border
                            has_touched_border = True
                        my_island.append([yk,xk])
                        local_q.append([yk,xk])
                        mask[yk][xk] = True
            # whenever this first BFS breaks, it means we got down to the whole island, and 
            # depending on if it is border touching or not, we will filp the O's or not 
            if not has_touched_border:
                for j, i in my_island:
                    board[j][i]='X' # overwriting
            





        