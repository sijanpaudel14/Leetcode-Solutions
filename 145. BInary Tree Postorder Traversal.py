class Solution(object):
    def postorderTraversal(self, root):
        """
        Perform preorder traversal of a binary tree.
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # Initialize an empty list to store the traversal result
        traversal_result = []
        
        # Define a helper function for the recursive traversal
        def traverse_postorder(current_node):
            # Base case: If the current node is None, stop the recursion
            if not current_node:
                return
            
            # Recursively traverse the left subtree
            traverse_postorder(current_node.left)
            
            # Recursively traverse the right subtree
            traverse_postorder(current_node.right)

            # Process the current node (visit the node)
            traversal_result.append(current_node.val)
        
        # Start the traversal from the root node
        traverse_postorder(root)
        
        # Return the result of the traversal
        return traversal_result
