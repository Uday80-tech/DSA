class Solution(object):
    def isPalindrome(self, x):
        num = x
        val = 0
        while num > 0:
            val = val*10 + num % 10
            num = num // 10
        if x == val:
            return True
        else:
            return False

        