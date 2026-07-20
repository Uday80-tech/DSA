class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(grid)
        m = len(grid[0])
        k = k % (m*n)
        ans = [[0 for i in range(m)]for j in range(n)]
        for i in range(n):
            for j in range(m):
                new_index = i*m + j + k
                ans[(new_index //m)%n ][ new_index % m] = grid[i][j]
        return ans