class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # ok so when permutating, our first element
        # can be any of the elements, but after picking
        # it is gone from the sample space
        # our real question is how to enforce that in a
        # reasonable space complexity (i.e not passing a 
        # local sub-array or mask to all of our paths )
        # maybe what we could do is whenever we walk a p
        # path remove that element, which takes O(n)
        # and then later put it back
        # to do this efficiently, we may want to use some kind of dict
        # + iterating over all of ours values and removing/adding
        # the pairs all in O(1)
        # here the keys don't really matter so they could effectivly
        # be the same as the values

        our_nums = {v:v for v in nums}
        # we have values as both our keys and value
        # here we don't really need pointer, as order doesn't
        # matter since tuples ordered differently are uique
        sol = []
        def backtrack(path):
            nonlocal our_nums
            if len(our_nums.values()) == 0:
                sol.append(path.copy())
                return
            # if we still have elements, we walk over them
            for num in list(our_nums.values()):
                # here we use list since we are not allowed to edit an array
                # on which we are iterating, to edit the real one and 
                # iterate over its copy
                store = our_nums.pop(num)
                path.append(num)
                backtrack(path)
                # cleaning up
                our_nums[num]=num
                path.pop()

        backtrack([])
        return sol






        