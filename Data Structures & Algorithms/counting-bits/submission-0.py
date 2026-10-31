class Solution:
    def countBits(self, n: int) -> List[int]:
        sol = []
        for num in range(n+1):
            res = 0
            while num:
                if num%2!=0: # i.e its lsb is a 1 as this is the only way to get 1
                    res+=1
                num = num >> 1 # right bitshift
            sol.append(res)
        return sol

        