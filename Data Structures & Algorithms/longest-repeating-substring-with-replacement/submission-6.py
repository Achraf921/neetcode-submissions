class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # when growing the window, the new most common character
        # can only be the one we've added
        # when shrinking our window, only if removing from 
        # most common we're at danger of changing most common
        # len - mc_count tells us if we match same char up to k

        char_counts = {}
        left = 0
        right = 0
        most_common_char = s[left]
        char_counts[s[left]] = 1
        max_len = 1
        while True:
            right = right + 1
            if right>=len(s): break # this is mostly for 1-long strings
            val = char_counts.get(s[right])
            if val is None:
                char_counts[s[right]] = 1
            else:
                char_counts[s[right]] = char_counts[s[right]]+1
            # we first update the char count on right movement, 
            # then since only that new character could 
            if char_counts[most_common_char]<char_counts[s[right]]:
                most_common_char = s[right]
            length = right - left + 1
            # scenario where it still fits
            if length- char_counts[most_common_char]<=k:
                if length>max_len:
                    max_len = length
            else:
                while True:
                    if s[left] == most_common_char:
                # in this scenario, we are removing from mc char, it could
                # hence be taken over by another character, and we hence
                # need to probe all other chars in the new substring to 
                # make sure a take-over hasn't happen
                        char_counts[s[left]] = char_counts[s[left]] - 1
                        left += 1
                        max_char = max(char_counts.items(), 
                        key = lambda x : x[1])[0]
                        if max_char != most_common_char:
                            most_common_char = max_char
                    # replacing in case another char tookover
                    else:
                        char_counts[s[left]] = char_counts[s[left]]-1
                        left+=1
                    length = right-left +1
                    if k>= length-char_counts[most_common_char]:
                        break
                    else:
                        continue
        return max_len










                