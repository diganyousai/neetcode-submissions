class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {'2': 'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if not digits:
            return []
        res = set()
        po = []
        def dfs(i, j):
            if i >= len(digits):
                if (''.join(po)) not in res:
                    res.add(''.join(po))
                return
            if j < len(hashmap[digits[i]]):
                po.append(hashmap[digits[i]][j]) 
                dfs(i+1,0)
                po.pop()
                dfs(i,j+1)
        dfs(0,0)
        return list(res)

