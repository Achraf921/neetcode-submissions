class TrieNode:
    def __init__(self, char, end_of_word : bool):
        self.char = char # our literal character
        self.end_of_word = end_of_word # our eow boolean
        self.nodes = [None] * 26 # 26 long

    def insert(self, next_node): # character insertion btw
        new_char = next_node.char
        isEOW = next_node.end_of_word
        idx = ord(new_char) - ord('a') # the char's index
        existing = self.nodes[idx]
        if existing is None:
            self.nodes[idx] = next_node
        else:
            if existing.end_of_word is False and isEOW is True:
                existing.end_of_word = True
            # otherwise we're already good and can move on


class PrefixTree:

    def __init__(self):
        self.root = TrieNode(None, False) # head is not a real node
        

    def insert(self, word: str) -> None:
        cur = self.root # we will be moving this pointer
        for c, i in zip(word, range(len(word))):
            if i==len(word)-1: #i.e last character
                cur.insert(TrieNode(c, True))
                # last step
            else:
                cur.insert(TrieNode(c, False))
                cur = cur.nodes[ord(c)-ord('a')] # moving the pointer forward
    # this should never fail


    def search(self, word: str) -> bool:
        cur = self.root
        for c, i in zip(word, range(len(word))):
            node = cur.nodes[ord(c) - ord('a')]
            if i == len(word)-1: # endinc scenario
                if node is None or node.end_of_word is False:
                    return False
                else:
                    return True
            else: # non-ending char, we just check existance
                if node is None: return False
                else: cur = node # we move forward
        

    def startsWith(self, prefix: str) -> bool:
        # similar than search, without the final end_of_word bool check on 
        # last character
        cur = self.root
        for c in prefix:
            node = cur.nodes[ord(c)-ord('a')]
            if node is None: return False
            else:
                cur = node
        return True # if all walking steps went fine and we got to the last one
        
        