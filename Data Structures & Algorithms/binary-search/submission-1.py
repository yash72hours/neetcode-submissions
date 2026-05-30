class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        nums.sort()

        for i, x in enumerate(nums):

            if x == target:
                return i
        
        return -1 
            