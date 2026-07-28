class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 设定初始目标为数组的最后一个索引
        goal = len(nums) - 1
        
        # 从倒数第二个元素开始，逆向遍历到第0个元素
        # range(start, stop, step)
        for i in range(len(nums) - 1, -1, -1):
            # 如果从当前位置 i 能够跳到（或超过）当前的目标 goal
            if i + nums[i] >= goal:
                # 更新目标为当前位置 i
                # 意味着只要能到达 i，就一定能到达原来的终点
                goal = i
                
        # 如果最终目标被移动到了起点（索引0），说明可以到达
        return True if goal == 0 else False
        