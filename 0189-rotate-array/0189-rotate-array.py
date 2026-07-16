class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,i,j):
            while i < j:
                nums[i] , nums[j] = nums[j] , nums[i]
                i += 1
                j -= 1
        n = len(nums)
        k = k % n
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-k-1)
        reverse(nums,0,n-1)
        