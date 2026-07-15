class Solution(object):
    def gcdOfOddEvenSums(self, n):
        num1 = (n * (1*2 + (n-1)*2))/2
        num2 = (n * (2*2 + (n-1)*2))/2
        while num1 != 0:
            rem = num2 % num1
            num2 = num1
            num1 = rem
        return num2