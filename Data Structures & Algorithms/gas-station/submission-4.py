class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # an ok-ish heuristic we could attempt is to always start at the 
        # cell which has the best delta between the gas it gives 
        # and the price to leave it let's compute those 
        # if the sum of the gas is below the sum of the cost it is un-solvable
        if sum(gas)<sum(cost): return -1
        # otherwise we want to pick the first element past negatives to accumulate the most
        # from the start before going into negatives

        # we want to do a moving sum to find the best starter
        total = 0
        res = 0
        for i in range(len(gas)):
            total+=(gas[i]-cost[i])
            if total<0:
                total=0
                res = i+1

        return res
        # this is highkey a either you know it or you don't but we basically
        # take the first number that brings us a positive total, and if that sequence breaks
        # then we take on where it restarts
        # we basically want to find the start of a maximum sum subarray 