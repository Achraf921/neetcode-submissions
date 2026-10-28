class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # here it seem trivial how to turn this prblem definition into a DAG
        # where a lot of sub-problems would get repeated
        # and this is a 2D problem as the two states to track are the max
        # yield ahead of us and if we are allowed to buy or not ahead of us
        # let's try to implement this using memoization
        # (day, can_buy) -> best money when inbound with no-coin is the state we want

        memo = {}
        # is that 3D DP actually perhaps ??
        # actually can_buy is more of a day-skip rather than actual state 
        # so I'd converge towards 2D DP (my_coin, day)
        # actually the can_buy boolean is just a flag to skip, so we could skip right away
        # by going day+2, hence simplifying
        def memo_search(my_coin, day):
            if day>len(prices)-1:
                return 0
            if day == len(prices)-1:
                if my_coin is not None: result = max(0, prices[day]-my_coin)
                else : result = 0
                memo[(my_coin, day)] = result
                return result
            if (my_coin, day) in memo: return memo[(my_coin, day)]
            # if we can't buy, we should just move on to the next day 
            best_trade = 0
            if my_coin is None:
                # we could buy if we don't hold a coin (since 1 coin at a time)
                buy = memo_search(prices[day], day+1) # that coin ain't free
                skip = memo_search(None, day+1)
                # we could also skip
                best_trade = max(0, buy, skip)
            else: 
                # if we own a coin, we could either hold or sell, selling at loss is never
                # optimal, so we gate that first option on us actually making a profit
                sell = 0
                if prices[day]>my_coin:
                    cash = prices[day]-my_coin
                    sell = cash + memo_search(None, day+2) # we won't be able to buy 
                skip = memo_search(my_coin, day+1)
                best_trade = max(0, skip, sell)
            
            memo[(my_coin, day)] = best_trade
            return best_trade
        
        return memo_search(None, 0)

         



        