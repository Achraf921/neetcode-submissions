class Solution:
    def countSubstrings(self, s: str) -> int:
        # this pretty much amounts into counting 
        # all palindroms with two pointers as we did earlier
        # with our centered approach and adding the number of chacaters total

        def count_pali(l, r):
            count = 0 # since it will count one too many
            while l>=0 and r<len(s) and s[r]==s[l]:
                l-=1
                r+=1
                count+=1
            return count # adjusting for the extra one
        # now we want to count for all possible substrings, and 
        # run both the even and odd centers

        global_count = 1 # accounting for the last char we missed

        for i in range(len(s)-1): # we will run the final one by hand
            global_count+= count_pali(i,i)
            global_count+= count_pali(i,i+1)

        
        return global_count

        
        