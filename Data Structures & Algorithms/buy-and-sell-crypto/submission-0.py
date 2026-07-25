class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        windows = []
        maxpro = 0
        windows.append(prices[0])
        for i in prices[1:len(prices)]:
            if i >= windows[-1]:
                windows.append(i)
                maxpro = max(maxpro,i-windows[0])
            else:
                if min(windows) < i:
                    a = windows[0]
                    windows = []
                    windows.append(a)
                    windows.append(i)
                else:
                    windows = []
                    windows.append(i)
        return maxpro




        