class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        rec = [0]*numCourses
        course = [[] for _ in range(numCourses)]
        for i,j in prerequisites:
            course[j].append(i)

        def dfs(n):
            if rec[n] == 2:
                return True
            if rec[n] == 1:
                return False
            rec[n] = 1
            for m in course[n]:
                ju = dfs(m)
                if ju == False:
                    return False
            rec[n] =2
            return True

        for k in range(numCourses):
            if not dfs(k):
                return False
        return True





        
        