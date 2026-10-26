class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # here we need to utilize XOR, as for two same numbers, 
        # ex 1101 and 1101, 1101 XOR 1101 would yield 0000, 
        # and moreover the order in which we do those XOR ops is not important as 
        # it would eventually cancel out, and return the unique number
        # (btw this is easy to visualize when looking at the collumns of our numbers
        # in base 2 when stacked on top of another)
        # btw in python the XOR operator is the chinese hat ^

        acc = 0
        for n in nums:
            acc = acc ^ n
        return acc


        