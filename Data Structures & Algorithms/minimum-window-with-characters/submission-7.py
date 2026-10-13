class Solution:


    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s): return ""
        left, right = 0, 0 
        gt= {} # in python we can actually compare two dictionaries
        # and order doesn't matter, just k:v being the same !
        for c in t:
            val = gt.get(c)
            if val is None:
                gt[c]=1
            else:
                gt[c]=gt[c]+1
        sub = {}
        sub[s[left]] = 1
        best_left = 0
        best_len = len(s)+1
        if len(t) == 1 and sub == gt:
            return s[left]
        have = 1 if (gt.get(s[left])!=None and gt.get(s[left]) == 1) else 0
        need = len(gt) #number of distinct characters
        while True:
            right+=1
            if right>len(s)-1: break
            val = sub.get(s[right])
            if val is None:
                sub[s[right]]=1
            else:
                sub[s[right]]+=1
            # now we run the query on gt and check if it matches
            # with whatever keys we have
            val = gt.get(s[right])
            if val is not None and val == sub[s[right]]:
                have+=1
            doesMatch = have==need
            if not doesMatch:
                # we just want to keep expending right in that case
                continue
            else:
                length = right-left+1
                if length<best_len:
                    best_len = length
                    best_left = left
                
                while True:
                    # we shrink from left
                    # we want to check if we'll need to shrink need
                    val = gt.get(s[left])
                    # the only scenario we would need to shrink need 
                    # would be at exact count equality
                    haveShrink = True if (val is not None 
                    and (sub[s[left]] == val)) else False
                    left+=1
                    sub[s[left-1]]-=1# decrementing
                    if haveShrink: have-=1
                    doesMatch = need==have

                    if not doesMatch: # shrinking broke the 
                        break
                    else: #compare to current min_string and keep shrinking
                        length = right-left+1
                        if length<best_len:
                            best_len = length
                            best_left = left
                        continue
        if best_len == len(s) + 1:
            return ""     
        else:       
            return s[best_left:(best_left+best_len)]



                
        