class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # here we seem to be able to pick a number multiple times
        # so bruteforce is O(2^n)
        # hence, this is a 1D knapsack, where the only state we need to pass
        # is the remainder, let's try to first do it in top down memoization

        memo = {}

        def top_down(rem):
            if rem==0: return 1 # base case
            if rem in memo: return memo[rem]
            cases = 0
            for num in nums: # we attempt all possible combinations
                if rem-num>=0:
                    cases += top_down(rem-num)
            memo[rem]= cases
            return cases

        return top_down(target)
                

            