class Solution(object):
    def shuffle(self, nums, n):
        ans = []
        first = nums[:n]
        second = nums[n:]
        for i in range(n):
            ans.append(first[i])
            ans.append(second[i])
            
        return ans    
        