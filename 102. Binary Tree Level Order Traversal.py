from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val            # Node value
        self.left = left          # Left child node
        self.right = right        # Right child node

def levelOrder(root):
    """
    Perform level-order traversal of a binary tree.
    
    Args:
    root (TreeNode): Root of the binary tree.

    Returns:
    List[List[int]]: A list of lists, where each inner list contains 
                     the values of nodes at that level.
    """
    # If the tree is empty, return an empty list
    if not root:
        return []

    result = []  # List to store the final level-order traversal
    queue = deque([root])  # Queue to keep track of nodes at each level

    # While there are nodes to process in the queue
    while queue:
        level_size = len(queue)  # Number of nodes at the current level
        level_nodes = []  # List to store values of nodes at this level

        # Process all nodes at the current level
        for _ in range(level_size):
            node = queue.popleft()  # Get the next node in the queue
            level_nodes.append(node.val)  # Add its value to the level list

            # If the node has a left child, add it to the queue
            if node.left:
                queue.append(node.left)
            # If the node has a right child, add it to the queue
            if node.right:
                queue.append(node.right)

        # After processing the level, add the level list to the result
        result.append(level_nodes)

    return result
