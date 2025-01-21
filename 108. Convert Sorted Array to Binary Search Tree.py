# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        # Helper function to build the BST recursively
        def buildBST(left, right):
            # Base case: if the left index exceeds the right index, return None
            if left > right:
                return None
            
            # Choose the middle element to maintain balance
            mid = (left + right) // 2
            # Create a TreeNode with the middle element as the root
            root = TreeNode(nums[mid])
            
            # Recursively build the left subtree with the left half of the array
            root.left = buildBST(left, mid - 1)
            
            # Recursively build the right subtree with the right half of the array
            root.right = buildBST(mid + 1, right)
            
            return root
        
        # Call the helper function with the full range of the array
        return buildBST(0, len(nums) - 1)
