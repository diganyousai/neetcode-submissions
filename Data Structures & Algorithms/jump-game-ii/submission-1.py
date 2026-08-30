#BFS
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:  #l,r是bfs的一层，一层一层往下找到的一定最小步数
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res