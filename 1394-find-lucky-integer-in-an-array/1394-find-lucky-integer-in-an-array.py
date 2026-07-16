class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hash_map = {}
        for i in range(len(arr)):
            if arr[i] in hash_map:
                hash_map[arr[i]] += 1
            else:
                hash_map[arr[i]] = 1
        ans = -1
        for key , value in hash_map.items():
            if key == value:
                ans = key
        return ans
                
        
        