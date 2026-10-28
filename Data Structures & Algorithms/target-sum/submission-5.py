class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # bruteforce is O(2^n)
        # A 2D DP solution here may help, 
        # tracking the following key-value state
        # position, target -> count

        memo = {}

        def memo_search(position, t):
            if position>len(nums)-1: return 0
            if (position, t) in memo: return memo[(position, t)]
            if position == len(nums)-1:
                if t==nums[position] and t==-nums[position]: # this is an edge case for 0
                    memo[(position, t)]=2
                    return 2
                if t == nums[position] or t == -nums[position]:
                    memo[(position, t)]=1
                    return 1
                else:
                    memo[(position, t)]=0
                    return 0
            
            # otherwise let's roll out
            count = 0 

            # we can either add our positive self, or negative self, and take 1 step

            count+= memo_search(position+1, t-nums[position]) # positive pick
            count+= memo_search(position+1, t+nums[position]) # negative pick

            memo[(position, t)] = count
            return count

        return memo_search(0, target)

                    
                
        
        