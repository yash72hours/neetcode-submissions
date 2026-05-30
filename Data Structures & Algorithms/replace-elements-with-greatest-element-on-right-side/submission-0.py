class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        x = len(arr)

        for i in range(x-1):

            arr[i] = max(arr[i+1::])

        arr[-1] = -1

        return arr
            