class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        x = 0
        y = 0 

        for n in nums:
            if n == 1:
                x += 1
                if y < x:
                    y = x
            if n == 0:
                x = 0

        return y
        