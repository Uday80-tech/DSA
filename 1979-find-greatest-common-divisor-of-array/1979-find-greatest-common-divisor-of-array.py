class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = nums[0]
        b = nums[len(nums) - 1]
        while a !=0:
            b , a = a , b % a
        return b
        