class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # we sort of need to build a stride here, but it is kind of weird
        # the only elements that move in weird directions are the ones before the end 
        # of a, ok nvm, this is actually very weird/hard
        # we kinda need to build a walking rule that is pretty easy for all cells
        # except the corner ones, and the one below the seed (top left corner of 
        # whatver layer we're working with), one thing we may want to do is to hence
        # mayber run a for loop over the layers right,
        # but the fact that the matrix can be a m*n rather than always a square matrix 
        # makes it trickier to determine which layer to work with
        # now one thing we could try to do is use a recursive approach where 
        # we always start to right, walk while grabbing all el.. , wait
        # element don't move, we just walk and grab them
        # let's try to make this recursivly

        res = []
        h, w = len(matrix), len(matrix[0])
        # 01 11 10 00
        # mode = [0: forward, 1 downward, 2, leftward, 3, upward]
        # sice we're already running at O(m*n) space complexity, I think it is 
        # actually reasonable to spark a bit-mask of our matrix to not walk on something 
        # twice
        
        # 1 2 3
        # 3 4 4
        # 9 2 0 -->
        # 1 2 3
        bit_mask = set()

        # this would work for an at least 2x2 matrix
        def rec_crawler(seed_y, seed_x, y, x, mode): # with those 2 extra bits
            # we could technically encode all 4 directions
            print(y, x)
            if (y, x) in bit_mask: return
            res.append(matrix[y][x])
            bit_mask.add((y, x))
            if mode==0: #righwards
                if x+1>(w-1)-seed_x:
                    if y+1<=(h-1)-seed_y: # we reached the right end case:
                        rec_crawler(seed_y, seed_x, y+1, x, 1) # we now move downwards
                else:
                    rec_crawler(seed_y, seed_x, y, x+1, 0)
            if mode==1 : # downwards
                if y+1>(h-1)-seed_y:
                    if x-1>=seed_x:
                        rec_crawler(seed_y, seed_x, y, x-1, 2) # we now go leftwards
                else:
                    rec_crawler(seed_y, seed_x, y+1, x, 1)
            elif mode==2: #leftwards
                if x-1<seed_x:
                    if not (y-1 == seed_y and x==seed_x):
                        rec_crawler(seed_y, seed_x, y-1, x, 3) # upwards
                else:
                    rec_crawler(seed_y, seed_x, y, x-1, 2)
            elif mode==3: #upwards
                if y-1 == seed_y and x==seed_x:
                    rec_crawler(y, x+1, y, x+1, 0)
                else:
                    if y-1>seed_y:
                        rec_crawler(seed_y, seed_x, y-1, x, 3)
            return
        
        if h==w==1: return [matrix[0][0]]
        rec_crawler(0, 0, 0, 0, 0)
        return res




        