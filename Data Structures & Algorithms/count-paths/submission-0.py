class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grip = [[0]*m for _ in range(n)]
        grip[0][0] = 1
        for j in range(1, m):
            grip[0][j] = 1  # 第一行全为1（路径数）
        for i in range(1, n):
            grip[i][0] = 1  # 第一列全为1（路径数）
        for i in range(1,n):
            for j in range(1,m):
                grip[i][j] = grip[i-1][j] +grip[i][j-1]
        return grip[n-1][m-1]
        