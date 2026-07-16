class Solution(object):
    def gcdSum(self, nums):
        def gcd(Min,Max):
            while Min != 0:
                Max,Min = Min,Max%Min
            return Max
        Maxi = nums[0]
        for i in range(len(nums)):
            Maxi = max(Maxi,nums[i])
            nums[i] = gcd(nums[i],Maxi)
        nums.sort()
        i=0
        j=len(nums)-1
        sum = 0
        while i<j:
            sum = sum + gcd(nums[i] , nums[j])
            i += 1
            j -= 1
        return sum
