class CountSquares:
    # a potential square is 4 points
    # we can't really do memoization, un-less we introduce a notion of point id
    # to discriminate points that have the same position
    # however, there is no notion of sub-problem here, so trying to memoize is pointless
    # handing me 4 points, it is pretty easy to verify if it is a square (O(1))
    # or if we could make a square out of those 4 points
    # here the costly part is the trials, we need to try
    # [p1, p2, p3, p4, p5]
    # n*(n-1)*(n-2) -> O(n^3) bruteforce
    # reverse thinking doesn't really help, as the output space (possibility)
    # is not discrete
    # however, one way to make it discrete would be to record the max x and y's
    # that were ever inserted, and the minimum of those 2, would be the max 
    # square we could possibly make
    # and since x and y never go beyond 1000, I think it is actually pretty resonable 
    # to attempt
    # now as for the datastructure, we may want something to the like of a 
    # dictonary that goes (x, y) -> count
    # because since we're trying to count how many
    # squares we can make, and that points w/ the same x and y should be treated 
    # independently, we could hence count them, to make the lookup O(1)
    # let's build this

    

    def __init__(self):
        self.point_dict = {} # (x, y)=> count
        self.x_max = 0
        self.y_max = 0

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) in self.point_dict: self.point_dict[(point[0], point[1])]+=1
        else:
            if point[0]> self.x_max:
                self.x_max=point[0]
            if point[1]> self.y_max:
                self.y_max=point[1]
            self.point_dict[(point[0], point[1])]=1
        

    def count(self, point: List[int]) -> int:
        max_square_len = min(self.x_max, self.y_max)
        # now that we have our square, we want to try everything from 
        # len = 1 up to len = max_square, and there are 4 poissibilities of squares to spark
        # from us at each length
        x, y = point[0],point[1]
        count = 0
        for n in range(1, max_square_len+1):
            # us in bottom left         # us in top left              # us in bottom right      # us top-right
            pos=[[[x,y+n],[x+n,y+n],[x+n,y]],[[x+n,y],[x+n,y-n],[x,y-n]],[[x-n,y],[x-n,y+n],[x,y+n]],[[x-n,y],[x,y-n],[x-n,y-n]]]
            for p1, p2, p3 in pos:
                if (p1[0],p1[1]) in self.point_dict and (p2[0],p2[1]) in self.point_dict and (p3[0],p3[1]) in self.point_dict:
                    squares = self.point_dict[(p1[0],p1[1])]*self.point_dict[(p2[0],p2[1])]* self.point_dict[(p3[0],p3[1])]
                    count+=squares
        
        return count
    # runs in O(1) time, O(1) space


        
