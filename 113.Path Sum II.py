# Algorithm:
# The problem can be solved using Depth-First Search (DFS), where we explore each path from the root to the leaves and check if the sum of values along the path equals the given target sum.

    # DFS Traversal: Start from the root and traverse down the tree, reducing the target sum by the value of each node as we go.
    # Backtracking: If we reach a leaf node (node with no children), check if the remaining sum equals the node’s value. If it does, add the path to the result.
    # Path Tracking: Keep track of the current path, and when a leaf node is reached, add that path to the result.
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum): 
    # Step 1: Initialize result list to store valid paths
    result = []
    
    # Step 2: Helper function for Depth-First Search (DFS) traversal
    def dfs(node, current_path, current_sum):
        # Step 2.1: If the node is None, return (base case for recursion)
        if not node:
            return
        
        # Step 2.2: Add the current node's value to the current path
        current_path.append(node.val)
        current_sum -= node.val  # Subtract current node's value from the remaining sum
        
        # Step 2.3: If it's a leaf node and the remaining sum is 0, add the path to result
        if not node.left and not node.right and current_sum == 0:
            result.append(list(current_path))  # Append a copy of current path to result
        
        # Step 2.4: Recursively explore left and right children
        dfs(node.left, current_path, current_sum)
        dfs(node.right, current_path, current_sum)
        
        # Step 2.5: Backtrack - remove the current node from the path before returning
        current_path.pop()

    # Step 3: Start DFS from the root node with an empty path and targetSum
    dfs(root, [], targetSum)
    
    # Step 4: Return the result, which contains all the valid paths
    return result
