class Solution:
    def longestPalindrome(self, s: str) -> str:
        # this wierdly is a regualar two pointers trick to analyze each char
        # as the 'center' or 'semi-center' of a palindrom and keep the 
        # longest

        def check_palindrom(l, r): # i is the position
            pali = ''
            left, right = l, r
            # we want to try the left-centered one, the right-centered one
            # and then the middle option, and then iterate until any of the 
            # two pointers exit the array

            'bbbbc'
            while left>=0 and right<=len(s)-1 and s[left]==s[right]:
                left-=1
                right+=1 #incrementing
            return s[left+1:right] # since those didn't met the criteria
        

        # finally we want to run it on all chars
        #'a, v, c, d'
     #'a, v, c, d, d' # to slide 

        palin = s[0] # a char is always a palinfrom
        for i in range(len(s)):
            l = i
            r = i+1 if i<len(s)-1 else i
            even = check_palindrom(l, l)
            odd = check_palindrom(l, r)
            if len(even)>len(palin): palin = even
            if len(odd)>len(palin): palin = odd
            
        return palin
         

            


            



        