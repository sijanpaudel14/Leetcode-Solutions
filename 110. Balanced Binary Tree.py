# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Helper function to calculate height and check balance
        def checkHeight(node):
            # If we reach a leaf node, its height is 0, and it's balanced
            if not node:
                return 0
            
            # Check the height of the left subtree
            leftHeight = checkHeight(node.left)
            # If left subtree is unbalanced, return -1
            if leftHeight == -1:
                return -1
            
            # Check the height of the right subtree
            rightHeight = checkHeight(node.right)
            # If right subtree is unbalanced, return -1
            if rightHeight == -1:
                return -1
            
            # If the height difference between left and right subtrees is too large, return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1
            
            # Otherwise, return the height of this node
            return 1 + max(leftHeight, rightHeight)
        
        # If the helper function returns -1, the tree is not balanced
        return checkHeight(root) != -1
