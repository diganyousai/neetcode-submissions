class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longgg=[]
        long=0
        for i in s:
            if i not in longgg:
                longgg.append(i)
                long = max(len(longgg),long)
            else:
                m = longgg.index(i)
                if m < len(longgg):
                    longgg=longgg[(m+1):len(longgg)]
                    longgg.append(i)
                else:
                    longgg=[]
                    longgg.append(i)                
        return long

        