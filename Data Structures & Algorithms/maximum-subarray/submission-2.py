class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化最大和为数组的第一个元素
        # 这样做是为了处理数组全为负数的情况
        maxSub = nums[0]
        
        # 当前连续子数组的和
        curSum = 0
        
        for n in nums:
            # 贪心策略：如果之前的累加和小于0，说明它对后续没有贡献，
            # 反而是负担，所以直接丢弃（重置为0），从当前数字重新开始
            if curSum < 0:
                curSum = 0
            
            # 将当前数字加入累加和
            curSum += n
            
            # 更新全局最大和
            maxSub = max(maxSub, curSum)
            
        return maxSub

        