class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        # If the input node is None (i.e., the graph is empty), return None immediately
        if not node:
            return None
        
        # A dictionary to map the original nodes to their respective clones
        oldToNew = {}

        # Helper function to perform Depth-First Search (DFS)
        def dfs(node):
            # Base Case: If the node has already been cloned, return the cloned node from the oldToNew map
            if node in oldToNew:
                return oldToNew[node]
            
            # Create a new copy of the current node (clone it)
            copy = Node(node.val)  # Create a new node with the same value
            oldToNew[node] = copy  # Map the original node to its clone in the oldToNew dictionary

            # Now, recursively clone all of the current node's neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))  # Append each neighbor's clone to the neighbors list of the clone

            return copy  # Return the cloned node after all its neighbors have been cloned

        # Start the DFS traversal from the provided node
        return dfs(node)
