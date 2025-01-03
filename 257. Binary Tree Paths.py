class Solution:
    def binaryTreePaths(self, root):
        # Helper function to perform Depth-First Search (DFS)
        def dfs(node, path, paths):
            # Base case: If the current node is None, stop recursion
            if not node:
                return
            
            # Step 1: Add the current node's value to the current path string
            path += str(node.val)
            
            # Step 2: Check if the current node is a leaf (no left or right child)
            if not node.left and not node.right:
                # If it's a leaf, append the current path to the result list
                paths.append(path)
            else:
                # Step 3: If not a leaf, extend the path with "->" and continue recursion
                path += "->"  # Add the separator for further traversal
                dfs(node.left, path, paths)  # Recurse on the left child
                dfs(node.right, path, paths)  # Recurse on the right child
        
        # Initialize an empty list to store all root-to-leaf paths
        paths = []
        
        # Start DFS traversal from the root with an empty path
        dfs(root, "", paths)
        
        # Return the list of all root-to-leaf paths
        return paths
