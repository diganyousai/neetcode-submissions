class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(2**n):
            subset = [nums[j] for j in range(n) if (i & (1 << j))] #判断1用这个语句，前面不用补0，反正碰到0也不加元素
#这种subset的写法也不用初始化
            res.append(subset)
        return res



        