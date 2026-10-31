class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def power(x, n):
            if x==0: return 0
            if n==0: return 1
            else:
                res = power(x, n//2)
                res = res * res
                return x*res if n%2 else res
        
        if n>=0:
            return power(x, n)
        return 1/power(x, -n)
            

        


        