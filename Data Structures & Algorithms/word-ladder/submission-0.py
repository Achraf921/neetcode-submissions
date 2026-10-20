class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        # here the winning approach is actually to consider that the max len
        # of a word is 10 while the max len of the list is 100 (5000)
        # on leetcode
        # we'd hence rather build an adjacency list from all patterns of a word
        # and map words that match in O(n*m^2) rather than bruteforce the 
        # adjacency list in O(n^2 * m)

        # here, we should probably grab a word, build all patterns
        # and then see if the adj list does contain a bucket for such pattern
        # and if not create it and add ourselves to it

        pattern_adj = {}

        for word in [beginWord]+wordList+[endWord]:
            # now we want to run all possible patterns:
            for i in range(1, len(word)+1): # 0 to len-1
                if i==1:
                    pat = '*'+word[1:]
                elif i<len(word):
                    pat = word[:i-1]+'*'+word[i:]
                else: #last character
                    pat = word[:-1]+'*'
                # adding it to adj
                if pat in pattern_adj.keys():
                        pattern_adj[pat].append(word)
                else:
                    pattern_adj[pat] = [word]

        # this should build the graph in O(n*m^2)
        # and now, we simply need to BFS for shortest path
        # i.e we want to add all start word's possible patterns
        # a helper would be good for that

        def all_patterns(word):
            patterns=[]
            for i in range(1, len(word)+1): # 0 to len-1
                if i==1:
                    pat = '*'+word[1:]
                elif i<len(word):
                    pat = word[:i-1]+'*'+word[i:]
                else: #last character
                    pat = word[:-1]+'*'
                patterns.append(pat)
            return patterns
   

        queue = deque()
        queue.append((beginWord,1))
        visited = {beginWord} # we'll store strings in there
        while len(queue)>0:
            cur = queue.popleft()
            if cur[0] == endWord:
                return cur[1]
            patterns = all_patterns(cur[0])
            for pat in patterns:
                next_words = pattern_adj[pat]
                for word in next_words:
                    if word==endWord:
                        return cur[1]+1
                    else:
                        if word not in visited:
                            visited.add(word) # to not enqueu it if it fits
                            # another patern
                            queue.append((word, cur[1]+1))

        # if none every yielded a path, then one doesn't exist
        return 0



            


                



