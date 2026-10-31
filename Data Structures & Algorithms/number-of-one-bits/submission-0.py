class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n>0:
            if n % 2 !=0: # i.e last bit is a 1
                res+=1
            n = n >> 1 # bit shifting to the right till completely flushed all bit
        return res

        
        