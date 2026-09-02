class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        rec = []

        def dfs(start, tar):
            if tar == 0:
                res.append(rec[:])
                return

            for j in range(start, len(candidates)):
                if j > start and candidates[j] == candidates[j - 1]:
                    continue

                if candidates[j] > tar:
                    break

                rec.append(candidates[j])
                dfs(j + 1, tar - candidates[j])
                rec.pop()

        dfs(0, target)
        return res