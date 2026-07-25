class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        s = 0
        
        while i < j:
            # 1. 计算当前面积并更新最大值
            m = min(heights[i], heights[j])
            s = max(m * (j - i), s)
            
            # 2. 移动较短的那根柱子（短板效应）
            if heights[i] <= heights[j]:
                i += 1  # 左边短，左指针右移
            else:
                j -= 1  # 右边短，右指针左移
                
        return s



        