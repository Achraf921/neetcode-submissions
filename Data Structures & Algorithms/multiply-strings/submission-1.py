class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # lil helper: assuming only digit characters
        def convertToInt(n):
            res = 0
            for c in n:
                digit = ord(c)-48
                res *= 10
                res += digit
            return res
        
        return str(convertToInt(num1) * convertToInt(num2))


        