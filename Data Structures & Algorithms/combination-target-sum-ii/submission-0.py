class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # here, my idea is to sort, and then fold all duplicates into 
        # (num, count) tuples that we will use when backtracking to determine
        # if we're allowed to re-use or not such a value

        cand = sorted(candidates)
        passed = None
        fold_cand = []
        for i in range(len(cand)-1): # here i+1 should always be in bounds
            if cand[i] == cand[i+1]:
                if passed is None:
                    passed = (cand[i],2)
                else:
                    num, count = passed # unpackign
                    passed = (num, count+1) #incrementing count
            else:
                if passed is not None:
                    fold_cand.append(passed)
                    passed=None
                else: # i.e we had no streak going on
                    fold_cand.append((cand[i], 1))
        fold_cand.append(passed if passed is not None else (cand[-1],1))
        # so this should build our tuples
        # now let's try to properly backtrack with the without creating linearly 
        # dependant paths
        sol = []

        def backtrack(path, pointer):
            if sum(path) == target:
                sol.append(path.copy())
                return # we've reached end
            if pointer>len(fold_cand)-1 or pointer<0 or sum(path)>target: return
            # now we walk our option
            # first option is to walk and take if the count is at least one
            cur = fold_cand[pointer]
            if cur[1]>=1:
                path.append(cur[0])
                backtrack(path, pointer+1)
                path.pop()
            # now we could also walk and not take it in all scenarios
            backtrack(path, pointer+1)
            # finally the specific here would be to decrement the count, take and not walk
            # and then re-increment it, if we are above 0 ofc
            # for this path to be linearly indepenedent, we actually need to take at least 
            # two
            if cur[1]>=2:
                it, count = cur
                cur = (it, count-2)
                fold_cand[pointer]=cur # just to be sure that we do pass down the edited version
                path.append(cur[0])
                path.append(cur[0]) # we take two
                backtrack(path, pointer) # we take and stay
                # now we need to get back to our original value for other paths
                it, count = cur
                cur = (it, count+2)
                fold_cand[pointer]=cur # walking back the way we'd have pop the path
                path.pop()
                path.pop() # cleaning our shit up

        backtrack([],0)
        return sol



