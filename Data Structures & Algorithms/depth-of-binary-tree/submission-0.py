# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        count = 0

        if not root:
            return  0
        else:
            count += 1

        leftd = self.maxDepth(root.left)
        rightd = self.maxDepth(root.right)

        return count + max(leftd, rightd)

        

        
        