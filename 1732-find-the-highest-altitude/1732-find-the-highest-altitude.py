class Solution(object):
    def largestAltitude(self, gain):
        ans =[]
        sum = 0
        ans.append(sum)
        for nums in gain:
            sum = sum + nums
            ans.append(sum)
        return max(ans)
        
        