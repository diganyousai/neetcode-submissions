class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grip = [[0]*n for _ in range(m)]
        grip[0][0] = 1
        for j in range(1, m):
            grip[j][0] = 1  # 第一行全为1（路径数）
        for i in range(1, n):
            grip[0][i] = 1  # 第一列全为1（路径数）
        for i in range(1,n):
            for j in range(1,m):
                grip[j][i] = grip[j-1][i] +grip[j][i-1]
        return grip[m-1][n-1]
        