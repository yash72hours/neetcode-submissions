class Solution:
    def myPow(self, x: float, n: int) -> float:

        y = x  

        if n > 0: 

            for i in range(n - 1):
                x *= y

        elif n == 0:
            return 1

        else:
            for i in range((-1 * n) + 1):
                x /= y

        return x
        