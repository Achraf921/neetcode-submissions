class Solution:
    def isHappy(self, n: int) -> bool:
        # for a number to be happy, it should I suppse only be made up of a single 1 right 
        # as any other number would grow abnormously
        memo = set()
        def sum_squares(num):
            if num in memo: return False
            memo.add(num)
            st = str(num)
            acc = 0
            for c in st:
                acc += int(c)**2

            if acc ==1: return True
            else: return sum_squares(acc)
        
        return sum_squares(n)