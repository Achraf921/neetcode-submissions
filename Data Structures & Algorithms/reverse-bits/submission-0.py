class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        power = 31
        while n:
            if n%2==0: # i.e lsb is a 0, hence we want a 1
                n = n >> 1 
                power-=1
            else:
                result+= 2**power
                power-=1
                n = n >>1
        return result

        
        