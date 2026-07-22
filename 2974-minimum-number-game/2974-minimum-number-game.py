class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        alice = None
        bob = None
        nums.sort(reverse = True)
        while len(nums) >0:
            alice = nums.pop()
            bob = nums.pop()
            ans.append(bob)
            ans.append(alice)
        return ans


        