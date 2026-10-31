class Solution:
    def reverse(self, x: int) -> int:
        isNeg=False
        if x<0:
            x = -x
            isNeg=True
            
        s = str(x)
        r = ''
        for i in range(len(s)-1, -1, -1):
            r+=s[i]
        if int(r)>=2**31: return 0
        if isNeg:
            return - int(r)
        return int(r)
        
        