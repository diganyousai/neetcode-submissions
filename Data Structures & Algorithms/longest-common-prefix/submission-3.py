class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        fir = strs[0]
        res = ''
        for i in range(len(fir)):
            for j in strs[1:len(strs)]:
                if i < len(j) and j[i] != fir[i]:
                    return res
                if i >= len(j):
                    return res
            res += fir[i]
        return res
            
        