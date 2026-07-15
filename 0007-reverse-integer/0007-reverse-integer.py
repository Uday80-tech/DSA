class Solution(object):
    def reverse(self, x):
        nums = 0 

        sign = -1 if x<0 else 1
        x = x * sign
        while x > 0:
            nums = nums * 10 + x % 10
            x = x/10

        if nums > 2**31 - 1 or nums < -2**31:
            return 0
        return nums*sign