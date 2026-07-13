class Solution(object):
    def oddCells(self, m, n, indices):
        target = target = [[0 for _ in range(n)] for _ in range(m)]
        for i in indices:
            row = i[0]
            column = i[1]
            for j in range(n):
                target[row][j] += 1
            for k in range(m):
                target[k][column] += 1
        count = 0
        for i in target:
            for j in i:
                if j%2 != 0:
                    count += 1
        return count

        