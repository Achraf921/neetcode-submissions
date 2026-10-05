class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def innerDp(nums: List[int], acc, target):
            if not nums: return False
            for num in nums:
                if acc + num == target or num == target: return True
            return (innerDp(nums[1:], acc+nums[0], target) or innerDp(nums[1:], acc, target))



        sum = 0
        for num in nums:
            sum+=num
        if sum%2 != 0: return False
        else: return innerDp(nums,0 ,sum//2)
        