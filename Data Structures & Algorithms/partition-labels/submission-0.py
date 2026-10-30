class Solution:
    def partitionLabels(self, s: str) -> List[int]:
    # this is easily solvable with a 26-long dict-array for every 
    # char that will map to the first occurence of the character 
    # and its last occurence and from that we'll be able to 
    # build the contiguous substrings

        span_dict = [[-1,-1]] * 26
        for i, c in enumerate(s):
            index = ord(c)-ord('a')
            if span_dict[index][0]==-1: # first occurence
                span_dict[index] = [i,i]
            else: # it has already a starter we are just the rightmost one
                span_dict[index][1]=i
        # this should correctly build the dict, and we'll now re-walk the string
        # left to right
        # to build our substrings, and use the dict to know if we have any other
        # characters inside of our substring and hence would need to expand
        # (O(26) to check)
        pointer = 0
        res = []
        print('hey')
        while pointer<len(s):
            char = s[pointer]
            l = pointer
            r = span_dict[ord(s[pointer])-ord('a')][1]
            # this builds the seeded substring from the pointer's character
            # which we'll want to expand if containing any other characters
            i=0
            while i < 26:
                pair = span_dict[i]
                if pair[0]!=-1 and pair[0]<r:
                    if pair[1]>r:
                        r = pair[1]
                        i=0 # we want to start over to catch any ones that were prev
                    # iously superior
                i+=1
            res.append(r-l+1)
            pointer = r+1
        return res
            

        