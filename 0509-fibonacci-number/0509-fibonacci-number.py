class Solution(object):
    def fib(self, n):
        def fibo(n):
            if n <2:
                return n
            else:
                return fibo(n-1) + fibo(n-2)
        return fibo(n)
        
        