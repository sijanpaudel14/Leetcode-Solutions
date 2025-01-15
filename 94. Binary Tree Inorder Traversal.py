# Definition for a binary tree node.
# Using Recursion

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Initialize the result list to store the inorder traversal
        result = []

        # Helper function for DFS
        def dfs(node):
            # Base case: if the current node is None, return
            if not node:
                return
            
            # Recursively visit the left subtree
            dfs(node.left)
            
            # Visit the current node (root) and append its value to result
            result.append(node.val)
            
            # Recursively visit the right subtree
            dfs(node.right)

        # Start the DFS from the root
        dfs(root)

        # Return the result list containing the inorder traversal
        return result

# Using Iterative Approach
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Initialize result list and stack for iterative traversal
        result = []
        stack = []
        current = root
        
        # Traverse the tree
        while current or stack:
            # Push all left nodes onto the stack
            while current:
                stack.append(current)
                current = current.left
            
            # Pop from stack, visit the node
            current = stack.pop()
            result.append(current.val)
            
            # Move to the right subtree
            current = current.right
        
        # Return the inorder traversal result
        return result


