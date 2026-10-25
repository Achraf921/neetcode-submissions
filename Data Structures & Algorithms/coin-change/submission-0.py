class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # [1, 5, 7, 10] = 12, 
        # greedy : 10, 1, 1
        # optimal : 7, 5  so greedy can't be the approach
        # let's try to visualize this as a DAG
        # ok I think I got the recurrence relationship, let's try to put it 
        # into memoization

        memo = {} # this will be 2D DP btw, 
        # counting both the 'depth' and the picked value
        # btw we are allowed to re-pick the same coin
        
        def rec_min(val, target):
            if target-val<0:
                return float('+inf') # I want to use this since we'll be
                # using min
            if target-val==0:
                return 0 # good end
            if (val, target) in memo: return memo[(val, target)]
            shortest_path = float('+inf')
            for coin in coins:
                shortest_path = min(shortest_path, rec_min(coin, target-val))
            
            memo[(val,target)] = 1 + shortest_path
            return 1+shortest_path
        
        result = rec_min(0, amount)
        # we use this trick to sample all coins at first 
        # trial

        if result == float('+inf'): return -1
        else : return result
