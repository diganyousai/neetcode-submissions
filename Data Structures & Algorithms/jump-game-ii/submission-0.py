class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [1000000]*len(nums)
        res[0] = 0
        for i in range(len(nums)):
            for j in range(0,i):
                if j + nums[j] >= i:
                    res[i] = min(res[i], res[j]+1)
        return res[-1]


        