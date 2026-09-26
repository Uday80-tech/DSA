class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum=[]
        leftsum.append(nums[0])
        for i in range(1,len(nums)):
            a=nums[i]+leftsum[i-1]
            leftsum.append(a)
        n=len(nums)
        rightsum=[0]*n
        rightsum[n-1]=nums[n-1]
        for j in range(n-2,-1,-1):
            rightsum[j]=rightsum[j+1]+nums[j]
        for i in range(n):
            if rightsum[i]==leftsum[i]:
                return i 
        return -1
        