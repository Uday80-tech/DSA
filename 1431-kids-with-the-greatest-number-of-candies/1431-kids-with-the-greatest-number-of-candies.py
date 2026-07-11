class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans = [0]*len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                ans[i] = True
            else:
                ans[i] = False
        return ans            

        