class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # we want to first of all infer order from
        # a word to another, and compare to the existing ordering
        # how to build an ordering that would be easy to move/append to 
        # and easy to use to find out contradictions
        # if we have an array of len 26 order, and we insert every char 
        # in the current state of order, noticing a new ordering would
        # require either inserting and re-shuffling, appending
        # or returning "" if it breaks the observed order
        # let's just for now go with that approach and 
        # make sure we implement it semantically correctly first

        # after building this is actually a cycle detecton problem
        superiority_adj = {}
        inferiority_adj = {}
        charset = set()
        # adjacency list
        # let's build our charset for later disjoint set detection by simply running every char
        for word in words:
            for c in word:
                charset.add(c)

        def compare_words(superior, inferior): # which ever one is deemed 
            nonlocal superiority_adj, inferiority_adj
            # such by our dictionary
            pointer = 0 #we'll use for comparaison
            while pointer<len(superior) and pointer<len(inferior):
                if superior[pointer]==inferior[pointer]:
                    pointer+=1
                else:
                    break
            # when we reached dissequality:
            if pointer>=len(superior) or pointer>=len(inferior): 
                # it means we reached one of the ends, and we should just checj pre-fix consistency
                if len(superior)>len(inferior): return ''
             # same word or prefix doesn't tell us anything about order
            else:
                # we don't want to append something twice though
                if inferior[pointer] not in inferiority_adj.keys():
                    inferiority_adj[inferior[pointer]] = [superior[pointer]]
                else:
                    if superior[pointer] in inferiority_adj[inferior[pointer]]: return
                    inferiority_adj[inferior[pointer]].append(superior[pointer])

                if superior[pointer] not in superiority_adj.keys():
                    superiority_adj[superior[pointer]] = [inferior[pointer]]
                else:
                    if  inferior[pointer] in superiority_adj[superior[pointer]]: return
                    superiority_adj[superior[pointer]].append(inferior[pointer])

        
        # I actually see how this manifests a graph problem
        # we are actually sort of building here a superiority list
        # where for each char, we lock in whatever it is superior to
        # and we will later run cycle detetion using maybe Topological
        # sort, to see if the ordering makes sense graph-wide
        # we also may want to lookout for disjoint sets as those should
        # be considered on their own, and make ordering impossible
        # hence the 2nd part of this problem is probably some DSU for 
        # disjoint set detection followed by topological sort for cycle 
        # detection

        # now we want to run our function in fashion where we compare a string to all 
        # of its inferior strings, to build the widest adj list possble

        for i in range(len(words)): # left ot right
            sup = words[i]
            for j in range(i+1, len(words)): # all inferior words
                result = compare_words(sup, words[j])
                if result == '': return result
        
        # finally we want to add all chars that do not have any inferiors

        for char in charset:
            if char not in inferiority_adj.keys():
                inferiority_adj[char]=[] # nobody is superior to them
    
        for char in charset:
            if char not in superiority_adj.keys():
                superiority_adj[char]=[] # they at the bottom

        # we now have the full adjacency list, is there a way check for any disjoint sets 
        # without running a full DSU ?

        # well a quick way would just be to try to form the string
        # if we detect a cycle then disjoint set or not it is false
        # if we are able to build a string, we should compare its length to the len our our 
        # charset, and if different, it means that some part of the graph is inacessible 
        # and hence false right ?

        # let's implement BFS basedd topological sort (Khan's algorithm), with memoization
        # to either build the string or return ''

        # here it says 'any order' hence if faced with multiple topological orderings
        # it should be ok to return any if they exist

        # let's run Khan's algorithm

        topo_order = ''

        queue = deque()
        for v in inferiority_adj.keys():
            if len(inferiority_adj[v])==0:
                queue.append(v)

        print(queue)

        while len(queue)>0: # multi-source BFS
             cur = queue.pop()
             topo_order+=cur
             inferiors = superiority_adj[cur]
             superiority_adj.pop(cur)
             for char in inferiors: # all of its inferior elements
                isFree=True
                for sup in inferiority_adj[char]:
                    if sup in superiority_adj.keys():
                        isFree = False
                        break
                if isFree:
                    queue.append(char)
            # thats about it

        print(topo_order)
        print(charset)
        if len(topo_order)!= len(charset): return ''
        else: return topo_order





        