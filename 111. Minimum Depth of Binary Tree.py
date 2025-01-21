# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Helper function to calculate the minimum depth
        def getMinDepth(node):
            # If the node is None, return 0 (no depth)
            if not node:
                return 0
            
            # If the node is a leaf (no left and right children), return 1
            if not node.left and not node.right:
                return 1
            
            # Initialize minimum depth to a large value
            min_depth = float('inf')
            
            # If the left child exists, calculate its minimum depth
            if node.left:
                min_depth = min(min_depth, getMinDepth(node.left))
            
            # If the right child exists, calculate its minimum depth
            if node.right:
                min_depth = min(min_depth, getMinDepth(node.right))
            
            # Add 1 to include the current node
            return min_depth + 1
        
        # Call the helper function starting from the root
        return getMinDepth(root)
