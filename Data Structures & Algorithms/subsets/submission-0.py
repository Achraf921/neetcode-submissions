class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # let's do it recursively
        sol = [[]]
        def rec_subsets(arr, pointer):
            nonlocal sol
            if pointer>len(nums) -1: return
            else: cur = [nums[pointer]]
            result = arr + cur
            print(result)
            # let's now instantiate our decision tree and pass
            # all possible scenarios
            # first we add our current setup
            sol.append(result)
            # then we create all possible next setups
            # scenario where we don't take the element at our index
            rec_subsets(arr, pointer+1)
            # scenario wehre we do take the element at our index
            rec_subsets(result, pointer+1)
            # pointer moves regardless
            # this basically sparks two forks at every element,
        
        rec_subsets([],0)
        return sol