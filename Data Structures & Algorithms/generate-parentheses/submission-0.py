#回溯

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(pa,num,state):
            if state == 0 and num > state:
                pa += '('
                num -= 1
                state += 1
                dfs(pa,num,state)
                return
            if 0 < state < n and num > state:
                pa += '('
                num -= 1
                state += 1
                dfs(pa,num,state) 
                pa = pa[0:len(pa)-1]
                pa += ')'
                state -= 2
                dfs(pa,num,state)
            if state == num:
                while state:
                    pa += ')'
                    state -= 1
                res.append(pa)
                return                
        dfs('',2*n,0)
        return res

        