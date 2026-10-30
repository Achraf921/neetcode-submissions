class Solution:
    def checkValidString(self, s: str) -> bool:
        # ***)))
        # ((*)
        # Trying to come up with a rule/heuristic
        # we do want to count the openers and closers
        # with the usual rule of not closing when no open parenthesis exits
        # howver, we do want to allow that scenario if a wildcard could eventually
        # behave as the opener, and likewise, if at the end we have 
        # a remaining of wildcards and unclosed parenthsis, then the
        # wildcards could behave as closers
        #((*** works as * can also be an empty string
        # we also want to rule out something like
        # let's try to implement that greedy policy
        '''
        opener_counter = 0
        wildcard_counter = 0 # ((*)))

        for c in s:
            if c == '(': # we can always add an opener
                opener_counter+=1
            elif c == ')': # we want to either decrement the opener couter or wild
            # and if not possible return false
                if opener_counter>0:
                    opener_counter-=1 # we closed a parenthisis
                elif wildcard_counter>0:
                    wildcard_counter-=1 # we used a wildcard as an opener
                else:
                    return False
            else: # we have wildcard, we always take them 
                wildcard_counter+=1

        return opener_counter<=wildcard_counter # final wildcard condition on openers
        # this actually breaks on *(
        ''' # this fails
        leftmin, leftmax = 0, 0
        for c in s:
            if c == '(':
                leftmin+=1
                leftmax+=1
            elif c == ')':
                leftmin-=1
                leftmax-=1
            else: # wildcard, we can either take is as a ( to maximize or ) to minimize
                leftmin-=1
                leftmax+=1
            if leftmin<0:
                leftmin=0 # i.e if our decision was wrong to the point of causing
                # non-recoverable un-balance
            if leftmax<0:
                return False # even maxmimizing caused unbalance
        
        return leftmin==0

        