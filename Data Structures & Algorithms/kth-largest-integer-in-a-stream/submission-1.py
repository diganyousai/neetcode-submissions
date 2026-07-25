class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap 存储 K 个最大的元素
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)          # 原地堆化
        
        # 只保留 K 个最大的
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)      # 弹出最小值
    
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)    # 插入新值
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)      # 如果超过K个，弹出最小的
        return self.minHeap[0]               # 根就是第K大元素



        
