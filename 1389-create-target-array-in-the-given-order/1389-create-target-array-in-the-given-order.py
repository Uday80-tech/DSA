class Solution(object):
    def createTargetArray(self, nums, index):
        ans = []
        j = 0
        for i in index:
            ans.insert(i,nums[j])
            j = j + 1
        return ans

        