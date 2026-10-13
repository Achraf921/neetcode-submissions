class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack_max = [0] * len(prices)
        # let's first fill min
        for i in range(len(prices)-1, -1, -1):
            if i is len(prices)-1: stack_max[i] = prices[i]
            else:
                stack_max[i] = max(prices[i], stack_max[i+1])
        max_profit = 0
        for i in range(len(stack_max)):
            max_profit = max(max_profit, stack_max[i]-prices[i])
        return max_profit

# let's try walking this quick example and two edge cases
# 1) [2,5,7,34,32,2]
# stack_max = [34, 34, 34, 34, 32,2]
# max_profit = 32

# 2) edge case monotonically shrinking
# [9 , 7, 7, 7, 6, 2, 1]
# stack_max = [9, 7, 7, 7, 6, 2, 1]
# max_profit = 0

# 3) single element edge case
# [3]
# -> returns 0, good
