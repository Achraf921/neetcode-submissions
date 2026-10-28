class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # this is actually not a greedy problem but a backtracking problem

        # the state we should keep is i -> can it take is to the flag

        memo = {}

        def memo_search(i):
            if i in memo: return memo[i]
            if i>=len(nums)-1: return True
            strength = nums[i]

            for j in range(i+strength, i-1, -1):
                if j==i:
                    # we want to return right away as it means that we either didn't have any strength
                    # or that we tried all of the jump strenghts and that none delivered
                    memo[i] = False
                    return False
                else: 
                    sol = memo_search(j)
                    if sol:
                        return True

            return False
        
        return memo_search(0)
                    




        