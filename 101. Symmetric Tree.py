# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Helper function to check if two trees are mirror images
        def isMirror(left, right):
            # Base case: both nodes are None, they are symmetric
            if not left and not right:
                return True
            # If one node is None and the other is not, not symmetric
            if not left or not right:
                return False
            
            # If the values of the `left` and `right` nodes are not equal, return False
            # This means the tree is not symmetric at this point
            if left.val != right.val:
                return False

            # Recursively check if the left subtree of the left node is a mirror of the right subtree of the right node
            # and if the right subtree of the left node is a mirror of the left subtree of the right node
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        
        # Edge case: if the tree is empty, it is symmetric
        if not root:
            return True
        
        # Check symmetry starting from the root's left and right subtrees
        return isMirror(root.left, root.right)



