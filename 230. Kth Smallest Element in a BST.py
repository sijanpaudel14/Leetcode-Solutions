# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Initialize the result variable and the counter
        # result will store the kth smallest value, and count will track the number of nodes visited
        self.result = None
        self.count = 0

        # Helper function to perform in-order traversal
        def in_order(node):
            if not node:
                return  # Base case: if the node is None, return immediately

            # Traverse the left subtree first (recursive call)
            in_order(node.left)

            # Visit the current node
            self.count += 1  # Increment the count as we visit a node
            
            # Check if we've found the kth smallest element
            if self.count == k:
                self.result = node.val  # Store the kth smallest value in result
                return  # Exit the function early since we found the result
            
            # Continue with the right subtree
            in_order(node.right)

        # Start the in-order traversal with the root node
        in_order(root)

        # After the traversal is complete, return the result
        return self.result
