class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        number=n
        while(True):
            product=1
            n=number
            while n:
                product=product*(n%10)
                n=n/10
            if product%t==0:
                break
            else:
                number+=1
        return number
        