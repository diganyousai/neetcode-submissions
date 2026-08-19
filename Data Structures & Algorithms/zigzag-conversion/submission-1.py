class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[0]*len(s) for _ in range(numRows)]
        res = ''
        num = numRows*2-2
        l = 0
        if numRows == 1:
            return s
        for i in range(len(s)):
            if i%num < numRows - 1:
                matrix[i%num][l] = s[i]
            if i%num == numRows - 1:
                matrix[i%num][l] = s[i]
                l += 1
            if i%num > numRows -1:
                matrix[num - (i % num)][l] = s[i]
                l += 1
        for j in range(numRows):
            for k in range(len(s)):
                if matrix[j][k] != 0:
                    res += matrix[j][k]
        return res


        