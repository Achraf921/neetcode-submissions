class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # let's first sort and foldleft as usual
        my_nums = sorted(nums)
        cand = []
        passed = None 
        # here goal is to create an array of tuples (val, count)
        for i in range(len(my_nums)-1):
            if my_nums[i] == my_nums[i+1]:
                if passed is None:
                    passed = (my_nums[i], 2)
                else:
                    val, count = passed
                    passed = (val, count+1)
            else:
                if passed is not None:
                    cand.append(passed)
                    passed = None
                else: cand.append((my_nums[i],1))

        # flushing since we excluded the last i's append
        if passed is None:
            cand.append((my_nums[-1],1))
        else:
            cand.append(passed)

        # now we have a oru left-folded list, let's backtrack on it
        sol = []
        def backtrack(path, pointer):
            print(f'pointer: {pointer}, len(cand)-1 : {len(cand)-1}')
            if pointer > len(cand)-1:
                sol.append(path.copy())
                return
            # we now want to walk all paths,
            # first path we take is the one where we don't take the current
            # element
            backtrack(path, pointer+1)
            # second one is exclusively for paths with counts>1 and we'll
            # do all paths
            val, count = cand[pointer]
            if count>1:
                for n in range(1, count+1, 1): # we start from one, otherwise
                # it would trigger duplicates
                    for _ in range(n):
                        path.append(val)
                    backtrack(path, pointer+1) #we walk after appending n times
                    for _ in range(n): # finally we pop n times
                        path.pop()
            else: # if count is 1, vanilla walk and take backtracking
                path.append(val)
                backtrack(path, pointer+1)
                path.pop()

        backtrack([],0)
        return sol

            




        