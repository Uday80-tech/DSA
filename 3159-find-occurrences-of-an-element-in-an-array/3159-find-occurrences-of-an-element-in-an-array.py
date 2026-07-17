class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        map = {}
        occurence = 0
        for i in range(len(nums)):
            if nums[i] == x:
                occurence += 1
                map[occurence] = i
        answer = [0] * len(queries)
        for i in range(len(queries)):
            if queries[i] in map:
                answer[i] = map[queries[i]]
            else:
                answer[i] = -1
        return answer
