class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # trying every single combination would probably grow in O(n^n) or even more
        # idea is to run all possible tuples from each triplet
        # as well as a fold-left - like running max
        # and if either ever yields the result then return, in a sort of exhaustive
        # counting way, this would run in something to the like 
        # of O(2n^2) ~ O(n^2) and O(1) space

        # [a, b, c, e], is sol is a, b , e , our solution doesn't work
        '''
        for triplet in triplets:
            us = triplet
            fold_left = [0,0,0]
            for t2 in triplets:
                pair = [max(us[0], t2[0]), max(us[1], t2[1]), max(us[2], t2[2])]
                if pair == target:
                    return True
                fold_left = [max(fold_left[0], pair[0]), max(fold_left[1], pair[1]), max(fold_left[2], pair[2])]
                if fold_left == target:
                    return True
        
        return False
        ''' # this obviously fails 
        # how about trying some reverse thinking, and look for the target numbers in some of the triplets
        # however we should make sure that the target number survives the mergers with other
        # targets right, i.e if I have a triplet that contains 7, then I should find at most 
        # 2 other triplets (to grab all of the target 3 elements)
        # such that 7 is the maximum of the mergers at index 1 for at most the two others
        # we also want to handle the cases where a triplet holds multiple or all of the target values 
        # as thoses cases could help a lot 

        target_triplets = [set(), set(), set()] # we want to have 3 sets to quickly identify if a triplet 
        # lives in 2 or 3 of our target sets, we'll store them by index from the triplets array

        for i, triplet in enumerate(triplets):
            if triplet == target: return True
            if triplet[0]==target[0] and triplet[1]<=target[1] and triplet[2]<= target[2]:
                target_triplets[0].add(i)
            if triplet[1]==target[1] and triplet[2]<=target[2] and triplet[0]<= target[0]:
                target_triplets[1].add(i)
            if triplet[2]==target[2] and triplet[0]<=target[0] and triplet[1]<= target[1]:
                target_triplets[2].add(i)
        # so now we have 3 sets that provide all of the triplets that match the target at their respective 
        # index, a brute-force solution would be to try all possible combinations
        # but maybe a more subtle way would be to filter out as we pick, triplets that 
        # could potentially merge... well actually how about filtering from selection
        # now that we have added filering for selection, if all of the sets contain at least one element
        # then at least on combination exists right ??
        return len(target_triplets[0])!=0 and len(target_triplets[1])!=0 and len(target_triplets[2])!=0
        