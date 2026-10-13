class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alphabet = [0] * 27
        for c in s1:
            alphabet[ord(c)-ord('a')]+=1
        left, right = 0, len(s1)-1

        sub_alphabet = [0] * 27
        for c in s2[left:right+1]:
                sub_alphabet[ord(c)-ord('a')]+=1
                # initial sub-alphabet
        while right<len(s2):
            if alphabet == sub_alphabet: # O(27) -> O(1)
                return True
            else:
                left+=1
                right+=1
                # since incrementing only changes two characters, 
                # rather than re-computing the whole thing, we 
                # just change at the new borders
                if right>len(s2)-1: break
                sub_alphabet[ord(s2[left-1])-ord('a')]-=1
                sub_alphabet[ord(s2[right])-ord('a')]+=1 # the only two changes we need
                
        return False