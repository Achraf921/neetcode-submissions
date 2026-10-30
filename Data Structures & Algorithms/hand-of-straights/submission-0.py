class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0: return False
        # once that we are certian that we CAN build sequences of that length, 
        # I'd just assume that my heuristic of always picking the minimum 
        # as the seed of my sequences will work
        # let's build our hashmap
        table = {}
        for num in hand:
            if num in table:
                table[num]+=1
            else:
                table[num] = 1
        # this should provide us a number->count table
        # and we want to enforce the policy of removing the key-val pair 
        # whenever a count of 0 is reached
        # now we want to build our groups
        for _ in range(len(hand)//groupSize):
            parent = min(table.keys()) # seeding with the remaining min at every iter
            if table[parent]==1:
                table.pop(parent)
            else:
                table[parent]-=1 # we should not forget to also pop/derement the parent
            for _ in range(groupSize-1): #-1 since the parent is the lead
                if (parent+1) in table: # here we want to pop it and continue
                    if table[parent+1]==1:
                        table.pop(parent+1)
                    else:
                        table[parent+1]-=1
                    parent = parent+1
                else:
                    return False
        return True



        