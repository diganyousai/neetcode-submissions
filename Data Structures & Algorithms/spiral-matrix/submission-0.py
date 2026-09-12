class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, n - 1
        t, b = 0, m - 1

        res = []

        while l <= r and t <= b:

            # 上
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1

            # 右
            for j in range(t, b + 1):
                res.append(matrix[j][r])
            r -= 1

            # 下
            if t <= b:
                for i in range(r, l - 1, -1):
                    res.append(matrix[b][i])
                b -= 1

            # 左
            if l <= r:
                for j in range(b, t - 1, -1):
                    res.append(matrix[j][l])
                l += 1

        return res