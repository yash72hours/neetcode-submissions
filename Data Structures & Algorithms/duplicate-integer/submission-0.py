class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = 0
        for i in (nums):
            for j in (nums):
                if i == j:
                    x = x + 1
        if x > len(nums):
            return True
        else:
            return False