class Solution:
    def climbStairs(self, n: int) -> int:
        # this involes tabulation, whenever we return
        # we sort of want to cache the returned values for int k
        # and whenever we get queried, we first want to check the 
        # memoization kv store to see if the result was not already computed

        memo = {}

        def memoized_climb(k):
            nonlocal memo
            if k in memo: return memo[k]
            if k > n: return 0
            if k == n: return 1

            response = memoized_climb(k+1) + memoized_climb(k+2)
            memo[k]=response # actively memoizing whenever we solve
            return response

        return memoized_climb(0)

        