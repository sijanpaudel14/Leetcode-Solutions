# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node, current_sum):
            if not node:
                return False
            current_sum -= node.val
            # Check if it's a leaf node and the sum is zero
            if not node.left and not node.right:
                return current_sum == 0
            # Check left and right subtrees
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)
        
        return dfs(root, targetSum)
