class Solution(object):
    def sequentialDigits(self, low, high):
        nums = [1,2,3,4,5,6,7,8,9]
        for i in nums:
            x = i % 10
            if x<9:
                nums.append(i*10+x+1)
        return [x for x in nums if low <= x <=high]
        