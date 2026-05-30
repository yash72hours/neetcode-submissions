class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix) - 1):

            if matrix[i][0] <= target < matrix[i + 1][0]:

                for j in range(len(matrix[i])):
                    if matrix[i][j] == target:
                        return True
                
                return False  # checked row fully

        # check last row
        for num in matrix[-1]:
            if num == target:
                return True

        return False  # ✅ always return something