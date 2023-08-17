class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # O(n + p)

        preReqMap = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            preReqMap[course].append(prereq)
        
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if preReqMap[course] == []:
                return True
            
            visit.add(course)

            for prereq in preReqMap[course]:
                if not dfs(prereq): 
                    return False
            visit.remove(course)
            preReqMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

