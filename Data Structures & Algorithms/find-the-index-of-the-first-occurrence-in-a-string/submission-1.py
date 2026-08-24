class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        fi = needle[0]
        for i in range(len(haystack)-l+1):
            if haystack[i] == fi:
                if l == 1:
                    return i
                for j in range(i+1,i+l):
                    if haystack[j] != needle[j-i]:
                        break
                    if j-i == l-1:
                        return i
        return -1
        