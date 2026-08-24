class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):  
            if nums[r] != nums[r - 1]:  #不满足，l不动，r继续跑
                nums[l] = nums[r]   #原地修改
                l += 1
        return l