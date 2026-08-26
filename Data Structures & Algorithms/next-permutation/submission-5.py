class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        bi = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                bi = i
                break
        if bi == -1:
            nums.sort()
        else:
            mi = float("inf")
            mu,nu = 0,0
            for j in range(bi+1,len(nums)):
                if nums[j] > nums[bi] and nums[j] - nums[bi] < mi:
                    mi = nums[j] - nums[bi]
                    mu,nu = nums[j],j
            p = nums[bi]
            nums[bi] = mu
            nums[nu] = p
            for k in range(bi+1, len(nums)):
                min_idx = k

                for l in range(k+1, len(nums)):
                    if nums[l] < nums[min_idx]:
                        min_idx = l

                nums[k], nums[min_idx] = nums[min_idx], nums[k]
            
            


        

        