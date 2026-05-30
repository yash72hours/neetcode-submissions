class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr = nums1 + nums2

        arr.sort()

        x = len(arr)

        if x % 2 == 0:
            return (arr[x//2 - 1] + arr[x//2]) * 0.5
        else:
            return (arr[x//2])