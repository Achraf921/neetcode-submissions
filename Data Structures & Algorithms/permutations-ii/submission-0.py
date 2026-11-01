class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        # we may want to go for a boolean mask as it would be cheaper
        # space wise
        mask = [True] * len(nums)

        def rec_permute(acc : tuple) -> None: # Python doesn't do TCO
            nonlocal result, mask
            for i, num in enumerate(nums):
                if not mask[i]: continue
                else:
                    mask[i]=False
                    init_len = len(acc)
                    passed =  acc + (num,)
                    rec_permute(passed)
                    # we clean up our mess for next loop iteration
                    mask[i]=True

            if len(acc)==len(nums):
                result.add(acc)
            return
        
        rec_permute(())
        return list(result)

        