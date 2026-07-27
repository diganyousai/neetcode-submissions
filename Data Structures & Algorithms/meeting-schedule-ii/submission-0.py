"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals: an array of meeting time intervals
    # @return: the minimum number of conference rooms required
    
    def minMeetingRooms(self, intervals):
        # 提取所有会议的开始时间和结束时间，并分别排序
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        res, count = 0, 0  # res记录最大同时进行的会议数，count记录当前正在进行的会议数
        s, e = 0, 0        # s和e分别是开始时间列表和结束时间列表的指针
        
        # 遍历所有会议的开始时间
        while s < len(intervals):
            # 如果当前最早开始的会议，早于当前最早结束的会议
            # 说明一个新的会议开始了，但之前还有个会议没结束，发生了重叠
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                # 否则说明当前有一个会议结束了，可以释放一个房间
                # (start[s] >= end[e]，注意等于号意味着一个会议结束的同时另一个开始，可以直接用同一个房间)
                e += 1
                count -= 1
            
            # 每次处理完事件后，更新全局的最大并行会议数
            res = max(res, count)
            
        return res
        