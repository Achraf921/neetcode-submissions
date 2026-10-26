class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            add = 0
            print(carry)
            if i==len(digits)-1: add = 1
            if add+carry+digits[i]<=9:
                digits[i]=add+carry+digits[i]
                carry=0 # flush
                break
            else:
                digits[i] = (add+carry+digits[i])-10
                carry=1

        if carry !=0:
            digits.insert(0,carry)
        return digits
        