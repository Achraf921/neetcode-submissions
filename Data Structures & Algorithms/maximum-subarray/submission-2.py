class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # this is I believe kandane's algorithm, we must keep a running max here, and keep the 
        # max from all running maxes
        maxes = []
        mins = []

        if len(nums) == 1: return nums[0]

        for i in range(len(nums)):
            if i == 0:
                maxes.append(nums[i])
            else:
                maxes.append(max(nums[i], maxes[i-1]+nums[i])) # we restart when worth it

        return max(maxes) 
        