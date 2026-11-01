class Solution:
    def tribonacci(self, n: int) -> int:
        # Tn+3 = Tn+2 + Tn+1 + Tn
        # Tn+4 = Tn+3 + Tn+2 + Tn+1
        def up_down_tri(k, a, b, c):
            if k==(n-3): return a+b+c
            else: return up_down_tri(k+1, a+b+c, a, b)
        
        if n==0: return 0
        if n==1: return 1
        if n==2: return 1
        else: return up_down_tri(0, 1, 1, 0)
        