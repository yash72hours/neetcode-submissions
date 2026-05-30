class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        a = 0

        for i, x in enumerate(heights):
            for j, y in enumerate(heights):

                area = abs(i-j) * min(x, y)

                if area > a:
                    a = area
                    
        return a