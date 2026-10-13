class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alphabet = [0] * 27
        for c in s1:
            alphabet[ord(c)-ord('a')]+=1
        left, right = 0, len(s1)-1
        while right<len(s2):
            sub_alphabet = [0] * 27
            for c in s2[left:right+1]:
                sub_alphabet[ord(c)-ord('a')]+=1

            if alphabet == sub_alphabet: # O(27) -> O(1)
                return True
            else:
                left+=1
                right+=1
        return False