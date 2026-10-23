class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # this actually sounds pretty easy, build an adjacency list
        # for all paths, and then sort all adjacency lists
        # or even better, don't insert if lex is smaller 
        # than the current option, and push out if not
        # to eliminate the need for sorting
        # ok, we my actually need to sort, as cycles are allowed

        adj = {}

        for ini, dst in tickets:
            if ini not in adj:
                adj[ini] = [dst]
            else:
                adj[ini].append(dst)

        for key in adj.keys():
            adj[key].sort(reverse=True) #, to make pop O(1)

        # we may want to do some backtracking, as taking a lexicographically
        # motivated "wrong turn" could return early

        # we hence need to run dfs here
        # actually oru backtracking approach did TLE, apparently, we need to use 
        # Hierholzer’s algorithm
        path = []
        def dfs(airport):
            if airport in adj.keys():
                while adj[airport]:
                    dfs(adj[airport].pop())
                path.append(airport)
            else:
                path.append(airport)

        dfs('JFK')

        return path[::-1]
                

            


            