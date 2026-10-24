class Solution:
    def climbStairs(self, n: int) -> int:
        # this involes tabulation, whenever we return
        # we sort of want to cache the returned values for int k
        # and whenever we get queried, we first want to check the 
        # memoization kv store to see if the result was not already computed
        '''
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
        '''
        # the solution above is the top-down/memoization solution
        # let's try to implement the bottom-up/tabulation version

        table = {} 

        def bottom_up_climb(k):
            nonlocal table
            one = 1 if k+1==n else 0 if k+1>n else table[k+1]
            two = 1 if k+2==n else 0 if k+2>n else table[k+2]
            me = one+two
            print(me)
            if k==0: return me
            else:
                table[k]=me
                return bottom_up_climb(k-1)



        return bottom_up_climb(n)

            


        