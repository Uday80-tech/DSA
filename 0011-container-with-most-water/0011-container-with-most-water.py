class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        i = 0
        j = len(height) - 1
        while i < j:
            
            area = (j - i) * min(height[i],height[j])
            maxarea = max(area,maxarea)
            if height[i] > height[j]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                i += 1
                j -= 1
        return maxarea


        