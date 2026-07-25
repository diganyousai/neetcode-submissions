class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # 1. 找到了目标
            if nums[mid] == target:
                return mid
            
            # 2. 判断哪一半是有序的
            # 情况A：左半部分 [l...mid] 是有序的
            if nums[l] <= nums[mid]:
                # 如果 target 在左半部分的范围内
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # 往左找
                else:
                    l = mid + 1  # 否则去右边乱序的部分找
            
            # 情况B：右半部分 [mid...r] 是有序的
            else:
                # 如果 target 在右半部分的范围内
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # 往右找
                else:
                    r = mid - 1  # 否则去左边乱序的部分找
                    
        return -1