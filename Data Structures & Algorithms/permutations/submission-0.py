class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        rec = [False]*n
        res,per = [],[]
        def dfs(i):
            if i == n:
                res.append(per[:])
                return
            for j in range(n):
                if not rec[j]:
                    per.append(nums[j])
                    rec[j] = True
                    dfs(i+1)
                    per.pop()
                    rec[j] = False
        dfs(0)
        return res

        