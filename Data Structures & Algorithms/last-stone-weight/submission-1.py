class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1. 将所有元素取负数，从而利用 heapq 构建最大堆
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        # 2. 当堆中石头数量大于 1 时，继续粉碎
        while len(stones) > 1:
            # 弹出当前最重的两块石头（注意还原为正数）
            y = -heapq.heappop(stones)  # 最重的石头
            x = -heapq.heappop(stones)  # 第二重的石头
            
            # 3. 如果重量不相等，将差值重新放回堆中（记得取负数）
            if x != y:
                heapq.heappush(stones, -(y - x))
        
        # 4. 如果堆不为空，返回最后一块石头的重量（取反）；否则返回 0
        return -stones[0] if stones else 0

        