class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # this looks a whole lot like a sliding window problem, where 
        # we want to optimize the size of that sliding window
        if s == "": return 0
        longest = 1
        cache = {} # mapping is char -> it's index
        cache[s[0]] = 0
        left = 0
        for i in range(1,len(s)):
            right = i
            if s[right] not in cache or cache[s[right]]<left:
                cache[s[right]]=right
                if (right+1)-left>longest:
                    longest=(right+1)-left
            else:
                # here good thing is that we kept a char->position
                # hence our left will become the position right after
                # the one of the recorded duplicate and right will be 
                # be allowed in
                left = cache[s[right]]+1
                cache[s[right]] = right
                if (right+1)-left>longest:
                    longest=right+1-left
        return longest

                


        

        