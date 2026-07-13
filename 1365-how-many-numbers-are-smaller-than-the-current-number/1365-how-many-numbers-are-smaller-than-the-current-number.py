class Solution(object):
    def smallerNumbersThanCurrent(self, arr):
        if len(arr) == 0:
            return arr
        numtorank = {}
        sorted_array = arr[:]
        sorted_array.sort()
        rank = 0
        numtorank[sorted_array[0]] = rank
        for i in range(len(sorted_array)):
            if i > 0:
                if sorted_array[i] not in numtorank:
                    numtorank[sorted_array[i]] = i
                
                     
        for i in range(len(arr)):
            arr[i] = numtorank[arr[i]]
        
        return arr    

        
        