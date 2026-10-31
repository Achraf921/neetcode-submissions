class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter = 0
        for num in nums:
            counter+=num
        gt = 0
        for num in range(len(nums)+1):
            gt+=num
        return gt-counter

        