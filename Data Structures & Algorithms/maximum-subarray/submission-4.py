class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        sum1= nums[0]
        for i in nums:
            sum+=i
            if i >= sum:
                sum = i
            sum1 = max(sum1,sum)
        return sum1

        

        