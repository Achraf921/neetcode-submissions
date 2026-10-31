class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = False
        result = 0
        for i in range(32):
            aonebit = a%2==1
            bonebit = b%2==1
            if not aonebit and not bonebit and not carry: 
                a = a >> 1
                b = b >> 1
                continue
                # we don't add anything since already zero
            elif (aonebit and not bonebit and not carry) or (bonebit and not aonebit and not carry) or (carry and not aonebit and not bonebit):
                # this is the scenario where we just add one:
                result |= 1 << i
                if carry: carry = False
            elif (aonebit and bonebit and not carry) or (aonebit and carry and not bonebit) or (bonebit and carry and not aonebit):
                # we want to make it zero and make carry true:
                carry = True
            else: # all 3 are true
                result |= 1 << i
                carry = True # redundant but we explicit
            a = a >> 1
            b = b >> 1
        if result >= 2**31:
            result -= 2**32 # i.e if our first signed bit is one
        return result
                


        