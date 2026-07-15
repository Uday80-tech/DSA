class Solution(object):
    def reverse(self, x):
        nums = 0
        neg = False 

        if x < 0:
            neg = True
            x = 0 - x

        while x > 0:
            nums = nums * 10 + x % 10
            x = x/10

        if nums > 2**31 - 1 or nums < -2**31:
            return 0

        if neg:
            return -nums
        else:
            return nums