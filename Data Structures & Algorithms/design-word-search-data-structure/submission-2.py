class TrieNode:
    def __init__(self, char:str, eow:bool):
        self.char = char
        self.nodes = [None] * 26
        self.eow = eow
    def insert(self, node):
        next_char = node.char
        existing = self.nodes[ord(next_char)-ord('a')]
        if existing is None:
            self.nodes[ord(next_char)-ord('a')] = node
        



class WordDictionary:
    def __init__(self):
        # our root is always a 'blank' shot
        self.root = TrieNode(None, False)

    def addWord(self, word: str) -> None:
        cur = self.root
        for c,i in zip(word, range(len(word))):
            if i == len(word)-1:
                cur.insert(TrieNode(c, True))
            else:
                cur.insert(TrieNode(c, False))
                cur = cur.nodes[ord(c)-ord('a')]
        

    def search(self, word: str, starter=None) -> bool: #recursive + backtracking
        if word == "": return False
        if starter is None:
            cur = self.root
        else:
            cur = starter
        i = -1
        # here we will use a while loop since we actually need to 
        # explicitely control i 
        while i < len(word): 
            i+=1 # for continue reasons
            char = word[i]
            if char == '.':
                if i == len(word)-1: # i.e if this is the last char
                    for node in cur.nodes:
                        if node is not None and node.eow:
                            return True
                    return False
                     # if false, we are jumping off a cliff
                else: # backtracking scenario, less efficient
                    # we basically want to call every child node with whatever isn't
                    # a None ofc and our string minus the first dot
                    for node in cur.nodes:
                        if node is not None:
                            result = self.search(word[i+1:], node)
                            if result:
                                return True
                    return False # nothing was found after testing all paths
            else: # regular trie walking
                if cur.nodes[ord(char)-ord('a')] is None: return False
                else:
                    if i == len(word)-1: # last char and it did match
                        if cur.nodes[ord(char)-ord('a')].eow: # on last char
                            return True
                        else:
                            return False
                    else: # else we keep walking
                        cur = cur.nodes[ord(char)-ord('a')]
                            

        
