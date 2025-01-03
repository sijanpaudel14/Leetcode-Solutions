class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        # This will store the global maximum path sum
        self.max_sum = float('-inf')

        def dfs(node):
            # Base case: if the node is None, return 0 (no contribution)
            if not node:
                return 0

            # Recursively find the maximum path sum for the left and right subtrees
            left_max = max(dfs(node.left), 0)  # If the left sum is negative, we take 0
            right_max = max(dfs(node.right), 0)  # Same for right subtree

            # Calculate the path sum that includes both left and right children
            # and the current node's value
            path_sum = node.val + left_max + right_max

            # Update the global maximum if needed
            self.max_sum = max(self.max_sum, path_sum)

            # Return the maximum sum of the path going down from this node
            # (either going left or right, whichever is greater)
            return node.val + max(left_max, right_max)

        # Call dfs on the root node
        dfs(root)
        
        # The global maximum path sum is stored in self.max_sum
        return self.max_sum
