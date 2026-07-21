class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        product = 1
        while n > 0:
            d = n % 10
            sum += d
            product = product * d
            n = n / 10
        return product - sum