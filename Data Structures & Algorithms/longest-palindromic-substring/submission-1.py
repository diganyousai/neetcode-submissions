class Solution:
    def longestPalindrome(self, s: str) -> str:
        i,j = 0,0
        leng = 1
        res = []
        for st in range(len(s)):
            if st-1 >= 0 and s[st-1] == s[st]:
                j,i = st-1,st
                while 0<j<len(s) and 0<=i<len(s)-1:
                    if s[i+1] == s[j-1]:
                        i += 1
                        j -= 1
                    else:
                        break
                if j-i+1 > leng:
                    leng = j-i+1
                    if res:
                        res.pop()
                    res.append(s[i:j+1])
            if st+1 <= len(s)-1 and s[st+1] == s[st]:
                j,i = st+1,st
                while 0<i<len(s) and 0<=j<len(s)-1:
                    if s[i-1] == s[j+1]:
                        i -= 1
                        j += 1
                    else:
                        break
                if j-i+1 > leng:
                    leng = j-i+1
                    if res:
                        res.pop()
                    res.append(s[i:j+1])
            if st+1 <= len(s)-1 and st-1 >= 0 and s[st-1] == s[st+1]:
                i,j = st-1,st+1
                while 0<i<len(s) and 0<=j<len(s)-1:
                    if s[i-1] == s[j+1]:
                        i -= 1
                        j += 1
                    else:
                        break
                if j-i+1 > leng:
                    leng = j-i+1
                    if res:
                        res.pop()
                    res.append(s[i:j+1])
        if not res:
            return s[0]
        return ''.join(res)


        