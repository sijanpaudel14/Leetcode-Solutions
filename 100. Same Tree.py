# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # If both nodes are None, they are the same
        if not p and not q:
            return True
        # If one of them is None or their values are different, they are not the same
        if not p or not q or p.val != q.val:
            return False
        # Check left and right subtrees recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
