class Solution(object):
    def addDigits(self, result):
        """
        :type num: int
        :rtype: int
        """
        if result / 10 < 0:
            return result
    
        while result / 10  > 0:
            n = result
            sum = 0
            while n >0:
                sum = sum + (n % 10)
                n = n / 10
            result = sum
        return result



        