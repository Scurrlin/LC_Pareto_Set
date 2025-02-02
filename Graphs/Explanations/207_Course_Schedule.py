class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Create adjacency list for course prerequisites
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Tracks nodes in the current DFS path
        visiting = set()

        def dfs(crs):

            # Cycle detected
            if crs in visiting:
                return False
            
            # Course has no prerequisites, safe to complete
            if preMap[crs] == []:
                return True

            # Mark course as visiting
            visiting.add(crs)
            for pre in preMap[crs]:

                # If a cycle is found, return False
                if not dfs(pre):
                    return False
            
            # Remove from visiting set after processing
            visiting.remove(crs)

            # Mark course as processed (memoization)
            preMap[crs] = []
            return True

        # Run DFS for all courses
        for c in range(numCourses):
            if not dfs(c):

                # Cycle detected → Not possible to finish all courses
                return False

        # No cycles detected → Can finish all courses    
        return True

# Time Complexity: O(N + E)
# Space Complexity: O(N + E)