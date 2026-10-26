class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we can re-use words
        # the bruteforce approach would be to 
        # either walk the dictionary, and for each word slide it into 
        # the string until it fit, remove that part of the string
        # and move on
        # but for dictionary with m words, string with n chars
        # it would likely cost O(n*m) time, but since words can be repeated
        # the problem could blow up to O((n^2)*m)
        # with a datastructure like a trie, checking for pre-fixes and then
        # working in the resulting after pop-ing the prefix could run
        # one thing we could do is go the oposite way
        # and try every substring to see if it is in the dict (using a hashset)
        # but it would also cost O(n^2) and we may need to backtrack
        # in case we picked the wrong ordering (which is also possible)
        # with the earlier part
        # we could also see this the other way around, and likewise to legos
        # see if we can build the word from the dictionary words
        # this seems to have more potential as it now becomes a choice tree
        # k-ary (k being vocabulary length), who'se brute force would be 
        # exponential but to which we may do memoization on
        # here it is easy to see how we would implement the bruteforce
        # but we want to see which state would allow us to memoize this

        # let's try to implement this by right-fitting our solutions 
        # and see if the post-fix fits to memoize them

        memo = {}
        # maybe we do want to memoize the starting index of whichever block
        # we added

        # we need to backtrack again as keeping as state the position and string fails
        # we need to keep i as state

        def memoized_search(i): # i is only necessary for base condition
            # position is NOT an index
            if i in memo: return memo[i]
            if i==len(s): return True  # empty string, base case
            for word in wordDict:
                if word == s[i:i+len(word)] and memoized_search(i+len(word)):
                    memo[i] = True
                    return True
                else:
                    continue

            memo[i] = False # postfix doesn't matter in false
            # very important for memoization
            return False and memoized_search(i+1) # if we never find a solution, we return false
        
        return memoized_search(0)

        # here the winning state only depended on i, and its ramification being all True
        # we must first verify that a true ramificaition exists from i all the way 
        # to the end before declaring it true
                    
            
                
        
        
        


        
        
        