class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # base case is not element chosen
        # all choices are available, there is no constraint
        # on picking it once
        # the constraint on result is that it must sum to 
        # a nuumber, so exceeding it fails
        # we backtrack by removing that number and trying another
        # one
        sol = []

        #! BTW all numbers are positive !!

        def rec_comb(path, pointer): 
            if pointer>len(nums)-1 or pointer<0: return
            
            elif sum(path) == target and path[-1] == nums[pointer]:
                # this second condition is to make sure only the
                # walk-less version gets added rather than the 
                # en passant (like in chess)
                    sol.append(path.copy())
                    # very crucial, we need to pass a copy/snapshot
                    # of current state rather than a ref
            elif sum(path) > target: return # we walked too much
            else:
                # as we walk with our pointer, we either take 
                # btw, we do get to take from
                # the element in front of us, or ourselves, or 
                # nothing, so let's walk all 3 paths :
                
                # we get to take our own value and either :
                # remain at our slot
                path.append(nums[pointer])
                rec_comb(path, pointer)
                # take and move is not an option as it 
                # creates a duplicate path, the same exact
                # can be achived by taking not moving
                # and then later moving without taking

                # other wise we also do get to move forward and 
                # not take it 
                path.pop()
                rec_comb(path, pointer+1)
                # not taking and remaining here is unproductive
                # so no need to do it

        rec_comb([],0)
        return sol

                