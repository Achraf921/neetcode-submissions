class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # this is very clearly a case for 2-D dynamic programming
        # let's try to write this up

        memo = {}

        def memo_search(y,x):
            if x == n-1 and y == m-1: return 1
            if (y,x) in memo: return memo[(y,x)]

            result = 0
            for j,i in [[y+1,x],[y, x+1]]:
                if j>=0 and j<=m-1 and i>=0 and i<=n-1:
                    result+= memo_search(j,i)
            
            memo[(y,x)] = result
            return result
        
        return memo_search(0,0)

        