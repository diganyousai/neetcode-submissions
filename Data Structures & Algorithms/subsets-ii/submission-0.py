class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]: #当你想不选的时候，你只能选到后面重复元素中的一个，而你担心的
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
        