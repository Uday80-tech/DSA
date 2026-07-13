class Solution(object):
    def arrayRankTransform(self, arr):
        if len(arr)==0:
            return arr
        numtorank = {}
        sorted_array = arr[:]
        sorted_array.sort()
        rank = 1
        numtorank[sorted_array[0]] = rank
        for i in range(len(sorted_array)):
            if i > 0:
                if sorted_array[i]>sorted_array[i-1]:
                    rank += 1
                    numtorank[sorted_array[i]] = rank
                elif sorted_array[i] == sorted_array[i-1]:
                     numtorank[sorted_array[i]] = rank
        for i in range(len(arr)):
            arr[i] = numtorank[arr[i]]
        
        return arr



        