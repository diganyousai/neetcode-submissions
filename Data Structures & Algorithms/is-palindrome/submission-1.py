class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(s)
        l1 = []
        for i in l:
            if 'A'<=i<='Z':
                j = chr(ord(i)+32)
                l1.append(j)
            elif '0'<=i<='9' or 'a'<=i<='z':
                l1.append(i)
        return l1 == l1[::-1]
