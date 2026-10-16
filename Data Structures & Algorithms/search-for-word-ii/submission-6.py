class TrieNode():
    def __init__(self, char:str):
        self.char = char
        self.nodes = [None] * 26
        self.word = None

# this time we truly don't need the eow field
    def insert(self, node):
        if self.nodes[ord(node.char)-ord('a')] is None:
            self.nodes[ord(node.char)-ord('a')] = node 

class Trie():
    def __init__(self):
        self.root = TrieNode(None) # blank

    def search(self, word:str)->bool:
        cur = self.root
        for c in word:
            if cur.nodes[ord(c)-ord('a')] is not None:
                cur = cur.nodes[ord(c)-ord('a')]
            else:
                return False
        return True # if we get here, it means all of our word's chars map to a path
    
    def insert(self, word:str):
        cur = self.root
        for c in word:
            cur.insert(TrieNode(c))
            cur = cur.nodes[ord(c)-ord('a')]
        cur.word = word



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # here we need to insert all of our words in the trie, and use the 
        # trie + mask to guide our walking and limit where we can walk
        guide = Trie()
        for word in words:
            guide.insert(word)

        # we also may want to pass trie nodes rather than the whole trie root

        
        h, w = len(board), len(board[0])
        def backtrack(path:str, y:int, x:int, mask:List[List[bool]], guide):
            if path == '':
                # this is the initalization scenario, we want to start a path from every
                # possible path at the beginning
                for j in range(h):
                    for i in range(w):
                        idx = ord(board[j][i])-ord('a')
                        if guide.nodes[idx] is not None:
                            mask[j][i] = False
                            path+= board[j][i]
                            backtrack(path, j, i, mask, guide.nodes[ord(board[j][i])-ord('a')])
                            path = path[:-1]
                            mask[j][i] = True
                            child = guide.nodes[idx]
                            if child.word is None and all(n is None for n in child.nodes):
                                guide.nodes[idx] = None
                return


            nonlocal final_sol
            if guide.word is not None: 
                final_sol.add(path)
                guide.word = None
                if len(path)>= max_len:
                    return # we insert non-empties at the beginning
            # 4 potential backtracking paths

            if y+1<h and mask[y+1][x] and guide.nodes[ord(board[y+1][x])-ord('a')] is not None:
                idx = ord(board[y+1][x])-ord('a') 
                mask[y+1][x] = False
                path+=board[y+1][x] 
                backtrack(path, y+1, x, mask, guide.nodes[ord(board[y+1][x])-ord('a')]) # we take
                path = path[:-1] # fixing our mess
                mask[y+1][x] = True
                child = guide.nodes[idx]
                if child.word is None and all(n is None for n in child.nodes):
                    guide.nodes[idx] = None

            if y-1>=0 and mask[y-1][x] and guide.nodes[ord(board[y-1][x])-ord('a')] is not None:
                idx = ord(board[y-1][x])-ord('a')
                mask[y-1][x] = False
                path+=board[y-1][x]
                backtrack(path, y-1, x, mask, guide.nodes[idx])
                path = path[:-1] # fixing our mess
                mask[y-1][x] = True
                child = guide.nodes[idx]
                if child.word is None and all(n is None for n in child.nodes):
                    guide.nodes[idx] = None
            
            if x+1<w and mask[y][x+1] and guide.nodes[ord(board[y][x+1])-ord('a')] is not None:
                idx = ord(board[y][x+1])-ord('a')
                mask[y][x+1] = False
                path+=board[y][x+1]
                backtrack(path, y, x+1, mask, guide.nodes[idx])
                path = path[:-1] # fixing our mess
                mask[y][x+1] = True
                child = guide.nodes[idx]
                if child.word is None and all(n is None for n in child.nodes):
                    guide.nodes[idx] = None

            if x-1>=0 and mask[y][x-1] and guide.nodes[ord(board[y][x-1])-ord('a')] is not None:
                idx = ord(board[y][x-1])-ord('a')
                mask[y][x-1] = False
                path+=board[y][x-1]
                backtrack(path, y, x-1, mask, guide.nodes[idx])
                path = path[:-1] # fixing our mess
                mask[y][x-1] = True
                child = guide.nodes[idx]
                if child.word is None and all(n is None for n in child.nodes):
                    guide.nodes[idx] = None

            return # base cases are those which can't walk no further
        
        initial_mask = [[True]* w for _ in range(h)] # all true initial mask
        final_sol = set()
        max_len = 0
        for word in words:
            if len(word)>max_len:
                max_len = len(word)
        print(max_len)
        backtrack('',0,0, initial_mask, guide.root)
        return list(final_sol)
            

            



        