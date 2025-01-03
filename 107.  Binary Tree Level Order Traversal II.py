from collections import deque

def levelOrderBottom(root):
    # Initialize the result list to store the final output (bottom-up order)
    result = []
    
    # If the root is None, return an empty list (edge case)
    if not root:
        return result
    
    # Initialize a deque (queue) to facilitate breadth-first search (BFS)
    queue = deque([root])
    
    # Perform BFS by processing each level of the tree
    while queue:
        # List to hold the nodes at the current level
        level = []
        
        # Get the number of nodes at the current level (this is 'level_size')
        level_size = len(queue)
        
        # Process all nodes at the current level
        for _ in range(level_size):
            # Dequeue a node from the front of the queue
            node = queue.popleft()
            
            # Append the node's value to the 'level' list (for the current level)
            level.append(node.val)
            
            # If the left child exists, enqueue it
            if node.left:
                queue.append(node.left)
            
            # If the right child exists, enqueue it
            if node.right:
                queue.append(node.right)
        
        # Append the current level's nodes to the result list
        result.append(level)
    
    # After BFS, the result has levels from top to bottom. Reverse it to get bottom-up order.
    return result[::-1]  # Reverse the list to achieve bottom-up order
