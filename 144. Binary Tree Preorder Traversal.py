class Solution(object):
    def preorderTraversal(self, root):
        """
        Perform preorder traversal of a binary tree.
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Initialize an empty list to store the traversal result
        traversal_result = []
        
        # Define a helper function for the recursive traversal
        def traverse_preorder(current_node):
            # Base case: If the current node is None, stop the recursion
            if not current_node:
                return
            
            # Process the current node (visit the node)
            traversal_result.append(current_node.val)
            
            # Recursively traverse the left subtree
            traverse_preorder(current_node.left)
            
            # Recursively traverse the right subtree
            traverse_preorder(current_node.right)
        
        # Start the traversal from the root node
        traverse_preorder(root)
        
        # Return the result of the traversal
        return traversal_result
