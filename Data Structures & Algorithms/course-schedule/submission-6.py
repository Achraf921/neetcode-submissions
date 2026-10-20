class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this is actually just a cycle detection on a directed graph
        # ok here, we actually need to use DFS - based topological sort
        # where we'll walk down the pre-req tree, with a set to not indulge in a cycle
        # if any cycle is detected we should return false
        # and we need to exploit memoization by making all courses that are proven solvable from no-prereq
        # courses up, we kinda use a in-order dfs here
        # we first need to build the dict/graph of all nodes and their pre-reqs


        myCourses = {}
        for course_num in range(numCourses):
            myCourses[course_num] = []
        # now we need to fill our arrays by walking the pre-req array
        for course, pre in prerequisites:
            myCourses[course].append(pre) # adding them, since they are unique
            # no need of watching out

        # now we want to run DFS on all nodes and memoize, such that we return directly if a sub-path
        # has been proven solvable instead of re-doing the work
        # let's try to do DFS recursively here as it makes more sense


        def rec_dfs(course, cache):
            # inorder, memoizing, 
            if course in cache: return False # base case of what we're trying to detect
            cache.add(course) # to avoid cycling back to it
            if len(myCourses[course])>0:
                for pre in myCourses[course]:
                    result = rec_dfs(pre, cache.copy())
                    if not result: # i.e if it returned false
                        # we do have a cycle below us
                        return False #
            # finally if we fully went through everythign without ever returning false, it means that every
            # single one of our pre-reqs solved and we hence have none, to properly memoize
            myCourses[course] = []
            return True # either we went down all of our pre-reqs and removed all of them where we hence
                        # return true, otherwise we dind't have any # base case too, and we return



        value = True
        for course in range(numCourses): # we want to run the DFS on all courses, here due to memoization 
        # we won't be repeating any work so this is still O(n)
            value = value and rec_dfs(course, set()) # passing in an empty hashset
        return value


            