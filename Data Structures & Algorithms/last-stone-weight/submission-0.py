class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            x = stones.pop()
            y = stones.pop()
            if y<x:
                stones.append(x-y)
                stones.sort()
        if len(stones) == 1:
            return stones[0]
        else:
            return 0

        