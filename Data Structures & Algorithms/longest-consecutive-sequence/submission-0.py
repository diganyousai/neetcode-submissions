class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
#Python 的 set 基于哈希表（Hash Table）实现。哈希表的核心优势是：
#通过哈希函数将元素映射到存储位置，使得查找、插入、删除操作的平均时间复杂度为 O(1)O(1) （理想情况下无哈希冲突时）
        