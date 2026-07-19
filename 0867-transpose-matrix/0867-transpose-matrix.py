class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])
        trans =[ [0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                trans[i][j] = matrix[j][i]
        return trans

        