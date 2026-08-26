class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:    #因为后面序列都是降序的，找到的第一个比nums[i]大的即是需要交换的
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]   #直接反转即可，跟i交换过值的那个点依然保持和左右的大小关系
            l += 1
            r -= 1