class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # [1 3, 7, 9] 28
        # 1-9- - 3 
        #  1  ... 1, 3 <-
        # 7 , 1..., 3 <-
        # 3.. 1, 3 <-
        # [18] = 6

        # I think a good memoization key-state pair could be the subproblem itself
        # taget -> combinations

        # moreover, we need a way to make sure we are not counting permutations, i.e 
        # 3,1 and 1,3 should not be counted as two separate results

        # a way to not count permutations would be to BFS only on elements 
        # that come after us in the coin sequence
        # such that all permutations of us and previous numbers are being counted by the 
        # previous number's bfs in a unique way

        # so I think the memo state is actually [position, target]
        # where it returns all existing combinations that add up to the target (variable)
        # starting and incluind digits [position:]
        # and settin poisition sort of should be additive

        memo = {}
        if amount==0: return 1

        def memo_search(position, target):
            if position>len(coins)-1: return 0
            if (position, target) in memo: return memo[(position, target)]
            if target<0: return 0
            if coins[position]==target:
                memo[(position, target)] = 1
                return 1
            # here we are in bounds, with no exisiting solution and below our target
            # we want to try out all of our >= options index-wise
            
            paths = 0
            # take n stay
            paths += memo_search(position, target-coins[position])

            # take n move
            #paths += memo_search(position+1, target-coins[position])
            # this step is a linear combination of the two others so it makes it overcount 
            # we should never have those kind of steps

            # skip n move
            paths += memo_search(position+1, target)
            
            memo[(position, target)] = paths
            return paths
        
        return memo_search(0, amount)


            







        