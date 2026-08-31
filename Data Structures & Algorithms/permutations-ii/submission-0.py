class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        used = [False] * n
        path = []
        res = []

        def dfs():
            if len(path) == n:
                res.append(path[:])
                return

            for j in range(n):
                if used[j]:
                    continue

                # 同层去重
                if j > 0 and nums[j] == nums[j - 1] and not used[j - 1]:
                    continue

                path.append(nums[j])
                used[j] = True

                dfs()

                path.pop()
                used[j] = False

        dfs()
        return res